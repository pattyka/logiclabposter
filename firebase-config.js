// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";

const firebaseConfig = {
    apiKey: "AIzaSyBuB42gcJc_pWQQJ1Fy9OH3NgpFdj68R50",
    authDomain: "logiclabwaitlist.firebaseapp.com",
    projectId: "logiclabwaitlist",
    storageBucket: "logiclabwaitlist.firebasestorage.app",
    messagingSenderId: "220641691358",
    appId: "1:220641691358:web:3541f84fda89298c2de44f",
    measurementId: "G-NWKPV5GW2G"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Firestore
const db = getFirestore(app);

export { db };
