// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";

const firebaseConfig = {
    apiKey: "AIzaSyDX_tUUYMvrUDZ_F_cbL716QCaKYJksmhQ",
    authDomain: "logiclab-kids-290f5.firebaseapp.com",
    projectId: "logiclab-kids-290f5",
    storageBucket: "logiclab-kids-290f5.firebasestorage.app",
    messagingSenderId: "490316514529",
    appId: "1:490316514529:web:4502ab76f42db3b34163a0",
    measurementId: "G-E8W35XPSZN"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Firestore
const db = getFirestore(app);

export { db };
