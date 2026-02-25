const menuBtn = document.getElementById('menuBtn');
const sidebar = document.getElementById('sidebar');
if (menuBtn && sidebar) {
  menuBtn.addEventListener('click', () => sidebar.classList.toggle('open'));
}

const deleteModal = document.getElementById('deleteModal');
if (deleteModal) {
  const confirmLink = document.getElementById('confirmDeleteLink');
  document.querySelectorAll('[data-delete-url]').forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      confirmLink.href = btn.dataset.deleteUrl;
      deleteModal.classList.add('open');
    });
  });
  deleteModal.querySelectorAll('[data-close-modal]').forEach((el) => {
    el.addEventListener('click', () => deleteModal.classList.remove('open'));
  });
}
