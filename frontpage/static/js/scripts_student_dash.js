document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('getLink')) {
        let btn_l = document.getElementById('getLink');
        btn_l.addEventListener('click', addLinkBlock);


        async function addLinkBlock() {
            let block_img = document.getElementById('block-link');
            block_img.setAttribute('style', "");
            window.location.replace("/monEspace#block-link");
        };
    };

    if (document.getElementById('getTickets')) {
        let btn_t = document.getElementById('getTickets');
        btn_t.addEventListener('click', addTicketBlock);


        async function addTicketBlock() {
            let block_img = document.getElementById('block-ticket');
            block_img.setAttribute('style', "");
            window.location.replace("/monEspace#block-ticket");
        };
    };
    if (document.getElementById('createTicket')) {
        let btn_u = document.getElementById('createTicket');
        btn_u.addEventListener('click', box_ticket);
        
        async function box_ticket(){
            let ticketContainer = document.getElementById("form-ticket")
            ticketContainer.setAttribute('style', "");
        };
    };
    if (document.getElementById('showTickets')) {
        let btn_u = document.getElementById('showTickets');
        btn_u.addEventListener('click', box_ticket_list);
        
        async function box_ticket_list(){
            let ticketContainer = document.getElementById("myTickets")
            ticketContainer.setAttribute('style', "");
        };
    };
    if (document.getElementById('sendTicket')) {
        let btn_u = document.getElementById('sendTicket');
        btn_u.addEventListener('click', box_ticket_list);
        
        async function box_ticket_list(){
            let formData = new FormData();
            formData.append('title', document.getElementById('ticket-title').value);
            formData.append('text', document.getElementById('ticket-text').value);
            formData.append('box', "ticket");
            let request = new Request('add_data', {method: 'POST', body: formData});
            fetch(request)
            .then(result => {
                window.location.replace('monEspace') //Convert response to JSON
            })
        };
    };
});