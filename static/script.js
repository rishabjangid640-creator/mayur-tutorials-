const counters=document.querySelectorAll(".counter")

counters.forEach(counter=>{

counter.innerText="0"

const update=()=>{

const target=+counter.getAttribute("data-target")
const c=+counter.innerText

const inc=target/200

if(c<target){
counter.innerText=Math.ceil(c+inc)
setTimeout(update,10)
}else{
counter.innerText=target
}

}

update()

})


const toggle=document.querySelector(".menu-toggle")
const nav=document.querySelector(".nav-links")

toggle.addEventListener("click",()=>{

nav.classList.toggle("active")

})
