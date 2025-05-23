from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Candidate
import pandas as pd
@login_required
def candidate_list_view(request):
    candidates = Candidate.objects.filter(company=request.user)
    return render(request, 'candidates/list.html', {'candidates': candidates})

@login_required
def candidate_create_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number', '')
        try:
            Candidate.objects.create(
                company=request.user,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number
            )
            messages.success(request, f'Candidate {first_name} {last_name} created successfully!')
            return redirect('candidates:list')
        except Exception as e:
            messages.error(request, f'Error creating candidate: {str(e)}')
    return render(request, 'candidates/create.html')

@login_required
def candidate_edit_view(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id, company=request.user)
    if request.method == 'POST':
        candidate.first_name = request.POST.get('first_name')
        candidate.last_name = request.POST.get('last_name')
        candidate.email = request.POST.get('email')
        candidate.phone_number = request.POST.get('phone_number', '')
        try:
            candidate.save()
            messages.success(request, f'Candidate {candidate.first_name} {candidate.last_name} updated successfully!')
            return redirect('candidates:list')
        except Exception as e:
            messages.error(request, f'Error updating candidate: {str(e)}')
    return render(request, 'candidates/edit.html', {'candidate': candidate})

@login_required
def candidate_delete_view(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id, company=request.user)
    if request.method == 'POST':
        candidate_name = f'{candidate.first_name} {candidate.last_name}'
        candidate.delete()
        messages.success(request, f'Candidate {candidate_name} deleted successfully!')
        return redirect('candidates:list')
    return render(request, 'candidates/delete_confirm.html', {'candidate': candidate})

@login_required
def candidate_upload_view(request):
    if request.method == 'POST':
        if 'manual' in request.POST:
            try:
                candidate = Candidate(
                    company=request.user,
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    email=request.POST['email'],
                    phone_number=request.POST.get('phone_number', '')
                )
                candidate.save()
                messages.success(request, 'Candidate added successfully!')
                return redirect('candidates:upload')
            except Exception as e:
                messages.error(request, f'Error adding candidate: {str(e)}')

        elif 'excel' in request.POST:
            try:
                excel_file = request.FILES['excel_file']
                df = pd.read_excel(excel_file)
                for _, row in df.iterrows():
                    Candidate.objects.create(
                        company=request.user,
                        first_name=row['first_name'],
                        last_name=row['last_name'],
                        email=row['email'],
                        phone_number=row.get('phone_number', '')
                    )
                messages.success(request, 'Candidates uploaded successfully!')
                return redirect('candidates:upload')
            except Exception as e:
                messages.error(request, f'Error uploading Excel: {str(e)}')

    return render(request, 'candidates/upload.html')