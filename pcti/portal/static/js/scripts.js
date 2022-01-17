$( document ).ready(function() {
    const deleteBtn = document.getElementsByClassName('delete-btn')

    var baseUrl   = 'http://localhost:8000/';
    // var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');

    $(deleteBtn).on('click', function(e) {

        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Todos itens relacioandos a este serão excluídos. Deseja realmente excluir?');

        if(result) {
            window.location.href = delLink;
        }

    });

    $(searchBtn).on('click', function() {
        searchForm.submit();
    });
});