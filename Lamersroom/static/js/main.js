$('.like-btn').on('click', function(evt) {
    let likeId = this.id;
    if (!likeId) {
        likeId = parent.id;
    }
    let likeValue = +evt.currentTarget.value;
    let currentLike = evt.currentTarget;
    let csrfToken = getCookie('csrftoken');
    let data = {
        'id': likeId,
        'csrfmiddlewaretoken': csrfToken,
    }
    let url = document.location.pathname;

    $.ajax({
        type: "POST",
        data: data,
        url: url, 
        success: function (response) {
            if (response == 'like-removed') {
                likeValue -= 1;
                // currentLike.setAttribute('class', 'like-btn');
            } else if (response == 'like-added') {
                likeValue += 1;
                // currentLike.setAttribute('class', 'like-btn liked');
            } else {
                alert('Зарегестрируйтесь!');
            }

        currentLike.setAttribute('value', String(likeValue));
        currentLike.lastChild.textContent = String(likeValue);
        },
        error: function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText);
        }
    })

})  


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}