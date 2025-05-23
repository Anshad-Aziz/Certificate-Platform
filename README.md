# 🎓 SaaS-Based Certificate Generation & Verification Platform

A web-based multi-tenant SaaS platform that enables companies to effortlessly generate, manage, and verify internship certificates online with unique IDs and QR codes.

## 🚀 Project Overview

This project aims to solve the manual and error-prone process of internship certificate creation by providing a complete digital solution. Companies can subscribe, upload templates, generate certificates in bulk, and recipients can verify them via a public portal.

## 🔍 Problem Statement

Internship certificates are often created manually, resulting in:
- Time-consuming and error-prone processes
- No centralized tracking or verification
- Non-scalable solutions for growing companies

This platform addresses these challenges by offering automation, online verification, and centralized management.

## 🎯 Objectives

- SaaS subscription-based platform
- Bulk certificate generation from templates
- QR-code based certificate verification
- Dashboard and analytics for companies
- Admin control panel for platform monitoring

## 👤 Target Users

- **Super Admin:** Platform owner who manages plans and companies.
- **Company Admin:** Clients who generate and manage certificates.
- **Recipient/Verifier:** Users who receive or verify certificates.

## ⚙️ Key Features

### 🔐 Authentication & User Management
- Company registration, login/logout, password reset

### 🧾 Subscription & Pricing
- Tiered plans (50, 100, 100+ certificates/month)
- Plan renewal and upgrade support

### 🖼 Template Management
- Upload PDF/DOC templates
- Define dynamic fields (e.g., Name, Date)

### 👨‍🎓 Candidate Management
- Add candidates via form or Excel upload
- Edit/delete/search candidates

### 📄 Certificate Generation
- Auto-generate certificates with unique IDs and QR codes
- Download or email PDFs

### ✅ Verification Module
- Public portal for certificate authenticity checks via ID or QR scan

### 📊 Company Dashboard
- Usage statistics
- Most used templates
- Certificate trends

### 🛠 Admin Panel
- Manage companies, plans, and platform metrics
- Generate usage reports and handle verification overrides

## 🛠 Tech Stack

| Layer        | Technology               |
|-------------|--------------------------|
| Backend     | Python + Django          |
| Frontend    | HTML, CSS, JS (Bootstrap)|
| Database    | MySQL                    |
| PDF Gen     | ReportLab / WeasyPrint   |
| QR Codes    | Python `qrcode` library  |
| Versioning  | Git + GitHub             |

## 🗂 Suggested Milestones

| Week | Milestone                                             |
|------|--------------------------------------------------------|
| 1    | Requirements, DB Design, Project Setup                |
| 2    | User Auth, Subscription Models                        |
| 3    | Template Management                                   |
| 4    | Certificate Generation (from Excel)                   |
| 5    | QR Code + Verification                                |
| 6    | Dashboards & Reports                                  |
| 7    | Expiry Management + Profile Settings                  |
| 8    | Testing, Deployment, Presentation                     |

## 📦 Deliverables

- Functional Django web app (locally or hosted)
- GitHub repository with commit history
- Platform demo video
- Documentation:
  - ER Diagram & DB Schema
  - Module-wise walkthrough video
  - Setup instructions
    
[![Watch the Demo]](https://drive.google.com/file/d/1ocPVwqSKPzNStA_FK5AC5HiqKG5xGF40/view?usp=drive_link)


## 🔗 Reference

- Inspiration: [certifier.io](https://certifier.io/)

---

Feel free to fork, star ⭐, or contribute to improve this platform!

