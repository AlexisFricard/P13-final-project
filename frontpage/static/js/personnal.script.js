document.addEventListener('DOMContentLoaded', function() {

    if (document.getElementById('btn-photo')) {
        document.getElementById('btn-photo').addEventListener('click', function() {
            document.getElementById('box-photo-fs').setAttribute('style', 'display:flex');
        });
        document.getElementById('close-fs').addEventListener('click', function() {
            document.getElementById('box-photo-fs').setAttribute('style', 'display:none');
        });
    };


    if (document.getElementById("btn-cookie")) {
        let scrolling = 0
        let btnCookie = document.getElementById("btn-cookie")
        btnCookie.addEventListener("click", cookie_set)

        window.addEventListener('scroll', (event) => {
            if (scrolling == 0) {
                cookie_set()
                scrolling = 1
            }
        });
        async function cookie_set() {
            let cookieBar = document.getElementById('cookie-bar');
            cookieBar.setAttribute('style', "display: none;");
            let request = new Request('setcookie', {method: 'GET'});
            fetch(request);
        };
    };
    if (document.getElementById("show-form-ticket")) {
        let btnForm = document.getElementById("show-form-ticket")
        btnForm.addEventListener("click", show_form_ticket)

        async function show_form_ticket() {
            let form_ticket = document.getElementById('form-ticket');
            form_ticket.setAttribute('style', "display: block;");
        };
    };
    if (document.getElementById("show-list-tickets")) {
        let btnForm = document.getElementById("show-list-tickets")
        btnForm.addEventListener("click", show_tickets)

        async function show_tickets() {
            let list_ticket = document.getElementById('list-tickets');
            list_ticket.setAttribute('style', "display: block;");
            let form_ticket = document.getElementById('form-ticket');
            form_ticket.setAttribute('style', "display: block;");
        };
    };
});
