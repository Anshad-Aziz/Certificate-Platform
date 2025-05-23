document.addEventListener('DOMContentLoaded', function() {
    // Weekly Certificates Chart (Bar)
    const weeklyData = JSON.parse('{{ weekly_data|escapejs }}');
    const weeklyChart = new Chart(document.getElementById('weeklyChart'), {
        type: 'bar',
        data: {
            labels: weeklyData.map(item => item.week),
            datasets: [{
                label: 'Certificates Issued',
                data: weeklyData.map(item => item.count),
                backgroundColor: '#FFC107',
                borderColor: '#FFD54F',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: { beginAtZero: true }
            }
        }
    });

    // College Distribution Pie Chart
    const collegeData = JSON.parse('{{ college_distribution|escapejs }}');
    const collegePieChart = new Chart(document.getElementById('collegePieChart'), {
        type: 'pie',
        data: {
            labels: collegeData.map(item => item.college || 'Unknown'),
            datasets: [{
                data: collegeData.map(item => item.count),
                backgroundColor: ['#FFC107', '#FFD54F', '#FFECB3', '#FFF8E1', '#FFFFFF']
            }]
        },
        options: {
            plugins: {
                legend: { position: 'bottom' }
            }
        }
    });

    // Title Distribution Pie Chart
    const titleData = JSON.parse('{{ title_distribution|escapejs }}');
    const titlePieChart = new Chart(document.getElementById('titlePieChart'), {
        type: 'pie',
        data: {
            labels: titleData.map(item => item.title || 'Unknown'),
            datasets: [{
                data: titleData.map(item => item.count),
                backgroundColor: ['#FFC107', '#FFD54F', '#FFECB3', '#FFF8E1', '#FFFFFF']
            }]
        },
        options: {
            plugins: {
                legend: { position: 'bottom' }
            }
        }
    });
});