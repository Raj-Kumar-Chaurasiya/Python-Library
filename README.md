🏥 Hospital Management System – Frontend

A modern, responsive React + Vite frontend for a Hospital Management System.
This project includes fully functional UI pages such as Home, About Us, Services, Contact Us, Enquiry, Add Patients, and shared layout components like Header, Navbar, Footer, Slider, etc.

📌 Table of Contents

Overview

Features

Tech Stack

Project Structure

Installation

Running the App

Available Pages

Components

Scripts

Troubleshooting

Contributing

License

📖 Overview

This is the frontend UI for a Hospital Management System built with React + Vite.
It provides a fully responsive design for interacting with hospital-related services, patient registration, enquiries, and general information pages.

It is currently a UI-only project, and backend/API integration can be added later as needed.

⭐ Features

Fully responsive and modular component structure

Modern React with hooks

Vite for fast development and optimized builds

Organized pages:

Home

About Us

Services

Contact Us

Add Patients

Enquiry

Shared UI components (Navbar, Header, Footer, Slider)

Clean folder structure

Ready for backend API integration

🧰 Tech Stack
Layer	Technology
Frontend Framework	React
Bundler / Dev Server	Vite
Language	JavaScript / JSX
Styling	CSS
Package Manager	npm / yarn
📁 Project Structure
Hospital/
└── Frontend/
    └── hospital/
        ├── node_modules/
        ├── public/
        ├── src/
        │   ├── comman/
        │   │   ├── Header.jsx
        │   │   ├── Navbar.jsx
        │   │   └── Footer.jsx
        │   ├── general/
        │   │   ├── Home.jsx
        │   │   ├── AboutUs.jsx
        │   │   ├── Services.jsx
        │   │   ├── ContactUs.jsx
        │   │   ├── AddPatients.jsx
        │   │   └── Enquiry.jsx
        │   ├── Slider.jsx
        │   ├── index.css
        │   └── main.jsx
        ├── vite.config.js
        ├── index.html
        └── package.json

🛠️ Installation
1. Navigate to the project folder
cd Hospital/Frontend/hospital

2. Install dependencies
npm install

▶️ Running the App
Development Mode
npm run dev


The app will launch at:

http://localhost:5173

Build for Production
npm run build

Preview Production Build
npm run preview

🧭 Available Pages
🏠 Home

Main landing page including banners and slider.

ℹ️ About Us

Details about the hospital, mission, and vision.

🩺 Services

Shows a list of available hospital services.

📞 Contact Us

Includes a contact form and various communication options.

🧑‍⚕️ Add Patients

Form to add or register new patients (currently front-end only).

❓ Enquiry

Form for visitor enquiries and general questions.

🧩 Components
Component	Purpose
Header.jsx	Top section with brand/title
Navbar.jsx	App navigation
Footer.jsx	Footer with links/contact
Slider.jsx	Image slider on homepage
📜 Scripts
Command	Description
npm run dev	Run development server
npm run build	Build for production
npm run preview	Preview production build
🛠️ Troubleshooting
Node version mismatch

Ensure Node.js ≥ 16 (recommended: 18+)

“Module not found” errors

Run:

npm install

CSS not loading

Check correct import path in main.jsx:

import './index.css'

🤝 Contributing

Fork this repository

Create a new branch

Make changes

Submit a pull request

📄 License

Specify your license here — for example:

MIT License
© 2025 Your Name / Organization
