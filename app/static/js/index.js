const deleteButton = document.getElementById('btn');
const titleValue = deleteButton.getAttribute('title'); 
const noteId = parseInt(titleValue, 10)


deleteButton.addEventListener('click', () => {
    fetch(
        "/delete-note",
        {
            method: "POST",
            body: JSON.stringify({noteId: noteId})
        })
        .then((res) => {
            window.location.href = "/"
        })
})
