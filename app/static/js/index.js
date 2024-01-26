const noteForm = document.getElementById('noteForm');
const noteInput = document.getElementById('noteInput');
const notesList = document.getElementById('notesList');

noteForm.addEventListener('submit', (e) => {
    e.preventDefault(); 

     const noteText = noteInput.value.trim();
     if (noteText) {
        // Create a new list item for the note
        const listItem = document.createElement('li');
        listItem.className = 'list-group-item d-flex justify-content-between align-items-center';
        listItem.textContent = noteText;

        // Add delete button
        const deleteButton = document.createElement('button');
        deleteButton.className = 'btn btn-sm btn-danger';
        deleteButton.textContent = 'Delete';
        deleteButton.addEventListener('click', () => listItem.remove());

        listItem.appendChild(deleteButton);
        notesList.appendChild(listItem);

        // Clear the input field
        noteInput.value = '';
    }
});
