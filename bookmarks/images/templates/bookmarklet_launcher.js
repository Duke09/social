(function(){
    var rndm = Math.random()*9999999999;
    if (window.myBookmarklet != undefined){
        myBookmarklet();
    }
    else {
        document.body.appendChild(document.createElement('script')).src='https://127.0.0.1:8000/static/js/bookmarklet.js?r=' + Math.floor(rndm)
    }
})();