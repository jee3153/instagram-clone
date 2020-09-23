const usernameInput = document.getElementById("id_username")
const emailInput = document.getElementById("id_email")
const bioInput = document.getElementById("id_bio")
const passwordInput = document.getElementById("id_password")
const password1Input = document.getElementById("id_password1")
const password2Input = document.getElementById("id_password2")
const content = document.querySelector("section")
const saveBtn = document.getElementById("save")
const inputList = document.querySelectorAll("input")
const path = window.location.pathname
let message = document.querySelector(".message")

const loginOrRegisterOrSetting = (inputArr) => {
  if (path.includes("login")) {
    inputArr = [usernameInput, passwordInput]
  } else if (path.includes("register")) {
    inputArr = [usernameInput, password1Input, password2Input, emailInput]
  } else if (path.includes("setting")) {
    inputArr = [usernameInput, emailInput, bioInput]
  }
  for (let input of inputArr) {
    if (input == password1Input) {
      input.placeholder = "password"
    } else if (input == password2Input) {
      input.placeholder = "confirm password"
    } else {
      input.placeholder = input.name
    }
  }
}

// comment list align in one line
const fullText = (dom) => {
  const textList = document.querySelectorAll(dom)
  for (let text of textList) {
    text.onclick = (e) => {
      console.log(e.target)
      e.target.classList.toggle("truncate")
      e.target.classList.toggle("break-all")
    }
  }
}

// function execution
path !== "/" ? fullText(".comment") : null

if (
  path.includes("login") ||
  path.includes("register") ||
  path.includes("setting")
) {
  loginOrRegisterOrSetting()
}
