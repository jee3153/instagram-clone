const newPassword1 = document.getElementById("id_new_password1")
const newPassword2 = document.getElementById("id_new_password2")
const inputSizeAdaption = () => {
  const placeholder1 = (newPassword1.placeholder = "New password")
  const placeholder2 = (newPassword2.placeholder = "Confirm new password")
  const inputs = [newPassword1, newPassword2]
  for (let input of inputs) {
    input.style.width = "16rem"
  }
}
if (window.location.pathname.includes("set-password")) {
  inputSizeAdaption()
}
