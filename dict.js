function makerequest(apikey,word){
    var link='https://www.dictionaryapi.com/api/v3/references/collegiate/json/'
    link=link.concat(word).concat("/").concat("?key").concat("=").concat(apikey);
    fetch(link).then(resp=>resp.json())
    .then(function(data){
      console.log(data.response.venues);
    })
}

async function getword(word) {
    let init = {
        mode: 'cors',
        method: 'GET',
    }
    var d="proxy/"
    var e=document.getElementById(word).textContent
    console.log(e)
    console.log()
    d.concat(e)
    let resp = await fetch(d, init);
    return resp.json();
}
async function main(word) {
    let p = await getword(word);
    console.log(p)
}