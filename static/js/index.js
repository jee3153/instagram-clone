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

// profile size hander on time_feed.html
// const profileSizeHandler = () => {
//   const homeUrl = window.location.pathname
//   const profile = document.querySelectorAll(".profile")
//   if ((homeUrl === "/" || homeUrl.includes("/comments")) && profile) {
//     for (let p of profile) {
//       p.classList.add("profile-sm")
//     }
//   } else {
//     for (let p of profile) {
//       p.classList.add("profile-md")
//     }
//   }
// }

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

const commentAlign = () => {
  const pageTitle = document.querySelector("title")
  const commentContainers = document.querySelectorAll(".comment-container")
  const classArr = ["px-5", "py-2"]

  if (pageTitle.innerHTML.includes("Comment")) {
    for (let container of commentContainers) {
      container.style.gridTemplateColumns =
        "3rem 100px 1fr 30px 30px 50px 120px"
      for (let c of classArr) {
        container.classList.add(c)
      }
    }
  } else {
    for (let container of commentContainers) {
      container.style.gridTemplateColumns =
        "minmax(0, 100px) 1fr 30px 30px 50px 100px"
    }
  }
  return
}

// function execution
path !== "/" ? fullText(".comment") : null

commentAlign()
if (
  path.includes("login") ||
  path.includes("register") ||
  path.includes("setting")
) {
  loginOrRegisterOrSetting()
}
