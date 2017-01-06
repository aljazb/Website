document.addEventListener('DOMContentLoaded', main, false);

function main() {
    document.getElementById("submit_button").addEventListener("click", function(){
        var pass = document.getElementById("password_register").value;
        var confPass = document.getElementById("password_confirm_register").value;
        if (pass != confPass) {
            document.getElementById("password_match").innerHTML = "The password does not match the confirmation password.";
        } else {
            document.getElementById("password_match").innerHTML = "";
        }
    });
}