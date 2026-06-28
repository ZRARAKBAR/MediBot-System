let selectedImage = null;

// ================= SPLASH SCREEN =================
window.addEventListener("load", () => {
setTimeout(() => {
document.getElementById("splashScreen").style.display = "none";
document.getElementById("homepage").style.display = "block";
}, 3000);
});

// ================= CHAT OPEN =================
function openChat() {
document.getElementById("homepage").style.display = "none";
document.getElementById("chatContainer").style.display = "flex";
}

// ================= CHAT CLOSE =================
function closeChat() {
document.getElementById("chatContainer").style.display = "none";
document.getElementById("homepage").style.display = "block";
}

// ================= BUTTON EVENTS =================
const startBtn = document.getElementById("startChatBtn");
const heroBtn = document.getElementById("heroChatBtn");

if(startBtn) startBtn.onclick = openChat;
if(heroBtn) heroBtn.onclick = openChat;

// ================= ENTER KEY =================
document.getElementById("userInput").addEventListener("keypress", function(e){
if(e.key === "Enter"){
sendMessage();
}
});

// ================= IMAGE UPLOAD =================
document.getElementById("imageInput").addEventListener("change", function(e){

const file = e.target.files[0];

if(!file) return;

selectedImage = file;

const reader = new FileReader();

reader.onload = function(){
    document.getElementById("previewImg").src = reader.result;
    document.getElementById("previewBox").style.display = "flex";
};

reader.readAsDataURL(file);

});

// ================= REMOVE IMAGE =================
function removeImage(){
selectedImage = null;

document.getElementById("previewBox").style.display = "none";

document.getElementById("imageInput").value = "";


}

// ================= SEND MESSAGE =================
function sendMessage(){
    let fd = new FormData();
fd.append("msg", message);
fd.append("image", file); 

let input = document.getElementById("userInput");

let msg = input.value.trim();

if(msg === "") return;

addBubble(msg, "user");

input.value = "";

let loadingBubble = addBubble("MediBot is analyzing...", "bot");

fetch("/get",{
    method:"POST",
    body:new URLSearchParams({
        msg:msg
    })
})
.then(res => res.json())
.then(data => {

    loadingBubble.innerText = data.response;

    scrollToBottom();

})
.catch(error => {

    console.error(error);

    loadingBubble.innerText =
        "Unable to connect. Please try again later.";

});
```

}

// ================= ADD BUBBLE =================


```
function addBubble(text,type){
let div = document.createElement("div");

div.className = `bubble ${type}`;

div.innerText = text;

document.getElementById("chatlogs")
        .appendChild(div);

scrollToBottom();

return div;
}
```



// ================= AUTO SCROLL =================


```
function scrollToBottom(){
let chatlogs = document.getElementById("chatlogs");

chatlogs.scrollTop = chatlogs.scrollHeight;

}

// ================= SMOOTH SCROLL =================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {


anchor.addEventListener("click", function(e){

    e.preventDefault();

    const target =
        document.querySelector(this.getAttribute("href"));

    if(target){
        target.scrollIntoView({
            behavior:"smooth"
        });
    }

});

});

// ================= NAVBAR EFFECT =================
window.addEventListener("scroll", () => {


const navbar =
    document.querySelector(".navbar");

if(!navbar) return;

if(window.scrollY > 50){

    navbar.style.background =
        "rgba(15,23,42,.95)";

}else{

    navbar.style.background =
        "rgba(255,255,255,.08)";
}

});}
document.getElementById("imageInput").addEventListener("change", function(e){

    let file = e.target.files[0];
    if(!file) return;

    let reader = new FileReader();

    reader.onload = function(){

        let chatBox = document.getElementById("chatBox");

        let imgDiv = document.createElement("div");
        imgDiv.className = "message user";

        imgDiv.innerHTML = `
            <img src="${reader.result}" style="
                width:180px;
                border-radius:12px;
                margin-top:5px;
            ">
        `;

        chatBox.appendChild(imgDiv);

        chatBox.scrollTop = chatBox.scrollHeight;
    };

    reader.readAsDataURL(file);
});