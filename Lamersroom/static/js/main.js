let likeBtn = document.querySelector('.like-btn');

likeBtn.addEventListener('click', function() {
    let likes = +likeBtn.value;
    likes += 1;
    likeBtn.setAttribute('value', String(likes));
    likeBtn.lastChild.textContent = String(likes);
    console.log(likes);
})


