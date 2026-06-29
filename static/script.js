// ---------------- POST VALIDATION ----------------
function validatePost() {

    let post = document.getElementById("post_content").value;

    if (post.trim() === "") {
        alert("⚠️ Post cannot be empty!");
        return false;
    }

    alert("✅ Post uploaded successfully!");
    return true;
}


// ---------------- SHARE POST ----------------
function sharePost(postId) {

    let text = document.getElementById(postId).innerText;

    navigator.clipboard.writeText(text)
    .then(() => {
        alert("🔄 Post copied! Share anywhere 😄");
    })
    .catch(() => {
        alert("❌ Share failed");
    });
}


// ---------------- LOGIN VALIDATION ----------------
function validateLogin() {

    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;

    if (username.trim() === "" || password.trim() === "") {
        alert("⚠️ Fill all login details!");
        return false;
    }

    return true;
}


// ---------------- REGISTER VALIDATION ----------------
function validateRegister() {

    let username = document.getElementById("reg_username").value;
    let password = document.getElementById("reg_password").value;

    if (username.trim() === "" || password.trim() === "") {
        alert("⚠️ Fill all details!");
        return false;
    }

    if (password.length < 4) {
        alert("❌ Password should be at least 4 characters!");
        return false;
    }

    alert("🎉 Account created successfully!");
    return true;
}


// ---------------- FOLLOW BUTTON ----------------
function followMessage() {
    alert("👥 Followed successfully!");
}