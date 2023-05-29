
console.log("hello")

const url = window.location.href
const searchForm=document.getElementById('search-form')
const searchInput= document.getElementById('search-input')
const resultBox=document.getElementById('results-box')
const csrf= document.getElementsByName('csrfmiddlewaretoken')[0].value

const sendSearchData = (student) => {
    $.ajax({
        type:'POST',
        url:'/search/',
        data:{
            'csrfmiddlewaretoken':csrf,
            'student': student,
        },
        success: (res)=>{
            console.log(res.data)
            const data = res.data
            if (Array.isArray(data)){
                resultBox.innerHTML=""
                data.forEach(student =>{
                    resultBox.innerHTML += `
                        <a href="/profileView/${student.id}" class="item">
                            <div class="row mt-2 mb-2">
                                <div class="col-2">
                                    <img src="${student.image}" class="stuimg"/>
                                </div>
                                <div class="col-10">
                                    <h5>${student.name}<h5>
                                    <h5>${student.id}<h5>
                                </div>
                            </div>
                        </a>
                    `
                })
            }
            else{
                if(searchInput.value.length>0){
                    resultBox.innerHTML = `<b>${data}</b>`
                }
                else{
                    resultBox.classList.add('invisible')
                }
            }
        },
        error: (err) =>{
            console.log(err)
        }
    })
}


searchInput.addEventListener('keyup', e=>{
    console.log(e.target.value)

    if(resultBox.classList.contains('invisible')){
        resultBox.classList.remove('invisible')
    }

    sendSearchData(e.target.value)
})