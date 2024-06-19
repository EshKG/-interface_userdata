function getCookie(name) {
  let cookie = document.cookie.split('; ').find(row => row.startsWith(name + '='));
  return cookie ? cookie.split('=')[1] : null;
}

async function postData(url = "", data = {}) {
  // Default options are marked with *
  const response = await fetch(url, {
    method: "POST", // *GET, POST, PUT, DELETE, etc.
    mode: "cors", // no-cors, *cors, same-origin
    cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
    credentials: "same-origin", // include, *same-origin, omit
    headers: {
      "Content-Type": "application/json",
      'X-CSRFToken': getCookie('csrftoken')
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: "follow", // manual, *follow, error
    referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify(data), // body data type must match "Content-Type" header
  });
  return response.json(); // parses JSON response into native JavaScript objects
}

function changestatus(){
     const elements = document.querySelectorAll(".status");
     for(i=0;i<elements.length;i++){
          console.log(elements[i].getAttribute('id'));
          let el = elements[i].id;
          elements[i].addEventListener("change",function(){

          try{

              postData("/board/",{'id':el, 'status':event.target.value}).then((data) =>{

              console.log(data); // JSON data parsed by `data.json()` call
                               })
          } catch (error) {
              console.error('Error:' + error.message)
          }
          document.querySelector('#saver').classList.remove("st-hidden");

     })
     }

}


document.addEventListener('DOMContentLoaded', function(){
           changestatus();

})