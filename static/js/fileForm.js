// form handler
function imageFormHandler() {
  const url = window.location.pathname
  let prop = "profile"
  let imgInput = document.getElementById("id_profile")
  let form = document.forms.namedItem("profile")
  // if (!url.includes("setting")) {
  //   imgInput = document.getElementById("id_image")
  //   form = document.forms.namedItem("image")
  //   prop = "image"
  // }
  let formData = new FormData(form)
  let display = document.getElementById("profile_display")
  let defaultLabel = document.querySelector(".box__label")

  const SetAttr = () => {
    imgInput.setAttribute("data-icon", "camera_alt")
  }

  function defaultStyling() {
    defaultLabel.className = "box__label"
    imgInput.style.color = "#cbd5e0"
  }

  function fileNameHandler(file) {
    const name = file.name

    defaultLabel.innerHTML = name
    let width = defaultLabel.offsetWidth / 2
    defaultLabel.style.left = `calc(50% - ${width}px)`
  }

  function preventDefault(e) {
    e.preventDefault()
    e.stopPropagation()
  }

  function handleDrop(file) {
    // get data when dropping
    console.log(file.files[0])

    var data = file.files[0]
    file.getData("profile")
    imgDataToForm(data)
    console.log(formData.getAll(prop))
  }

  function textDataToForm() {
    dataArr = [usernameInput, bioInput]
    for (data of dataArr) {
      formData.set(data.name, data.value)
    }
  }

  function imgDataToForm(data) {
    formData.append(prop, data)
  }

  form.addEventListener("submit", function (e) {
    preventDefault(e)

    fetch(window.location.href, {
      method: "POST",
      body: formData,
      headers: new Headers(),
    })
      .then((res) => {
        if (res.status === 200 || res.status === 201) {
          res.json().then((json) => {
            // result shown on a page
            display.style.backgroundImage = `url(/media/${json.media})`
            defaultLabel.innerHTML = "Choose a file or drag it here."
            defaultLabel.style.left = "calc(50% - 106px)"
            message.classList.toggle("hidden", false)
            window.setTimeout(() => {
              message.classList.add("hidden")
            }, 3000)
            console.log(json)
          })
        } else {
          console.log(res.statusText)
        }
      })
      .catch((err) => console.error(err))
  })

  imgInput.onclick = (e) => {}

  imgInput.addEventListener(
    "change",
    function (e, data) {
      if (e.dataTransfer) {
        //file selected by drag and drop
        data = e.dataTransfer.files[0]
        fileNameHandler(data)
        // textDataToForm();
      } else {
        //file selected by click
        console.log(this)
        data = this.files[0]
        fileNameHandler(data)
        imgDataToForm(data)

        console.log(this.files[0])
      }
    },
    false
  )

  form.onchange = (e) => {
    textDataToForm()
  }

  imgInput.ondragstart = function (e) {
    e.dataTransfer.setData(prop, e.dataTransfer.files[0])
    e.dataTransfer.dropEffect = "copy"
  }

  document.ondrop = function (e) {
    preventDefault(e)
    defaultStyling()
    fileNameHandler(e.dataTransfer.files[0])
    handleDrop(e.dataTransfer)
  }

  imgInput.ondragover = function (e) {
    imgInput.style.color = "#718096"
    defaultLabel.className = "box__label text-gray-600"
    e.dataTransfer.dropEffect = "move"
  }

  imgInput.ondragleave = function () {
    defaultStyling()
  }

  SetAttr()
}

for (const node of inputList) {
  if (node.type === "file" && window.location.pathname.includes("setting")) {
    imageFormHandler()
  }
}
