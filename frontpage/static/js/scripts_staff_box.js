document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('addPhoto')) {
        let btn_t = document.getElementById('addPhoto');
        btn_t.addEventListener('click', addPhotoBlock);


        async function addPhotoBlock() {
            let block_img = document.getElementById('imgform');
            let logo_photo = document.getElementById('logoPhoto');
            block_img.setAttribute('style', "");
            logo_photo.setAttribute('style', "display: none;");
        };
    };
    /********* Error box *********/
    async function displayErrorBox(state) {
        let modalContainerF = document.createElement('div');
        modalContainerF.setAttribute('id', 'modal');
        let customBoxF = document.createElement('div');
        customBoxF.className = 'custom-box text-start';
        customBoxF.innerHTML = '<p class="fs-6 text-primary text-center"><strong>Erreur</strong></p></br>';
        customBoxF.innerHTML += '<p class="fs-6 text-primary text-center"><strong>La tâche n\'as pas été effectué</strong></p></br>';
        customBoxF.innerHTML += '<p class="fs-6 text-primary text-center"><strong>' + state + '</strong></p></br>';
        customBoxF.innerHTML += '</br><button class="btn my-1 mx-2 bg-primary text-light" id="modal-close">Ok</button>';

        modalContainerF.appendChild(customBoxF);
        document.body.appendChild(modalContainerF);
        document.getElementById('modal-close').addEventListener('click', async function() {
            modalClose();
        });

        async function modalClose() {
            while (modalContainerF.hasChildNodes()) {
                modalContainerF.removeChild(modalContainerF.firstChild);
            }
            document.body.removeChild(modalContainerF);
        };
    };

    /********* Response User Box *********/
    async function displayPasswordBox(id, password, email) {
        let modalContainerP = document.createElement('div');
        modalContainerP.setAttribute('class', 'row px-0 w-25 justify-content-center')
        modalContainerP.setAttribute('id', 'modal');
        let customBoxP = document.createElement('div');
        customBoxP.className = 'custom-box text-start';
        customBoxP.innerHTML = '<p class="fs-6 text-primary text-center"><strong>Attention, message unique</br>Veuillez copier/coller les informations</br> ou les envoyer par email</strong></p></br>';
        customBoxP.innerHTML += (
            'Identifiant de connexion : <strong></br>' + id + '</strong></br>');
        customBoxP.innerHTML += (
            'Mot de passe : <strong></br>' + password + '</strong></br>');
         customBoxP.innerHTML += (
            '<a class="btn my-1 mx-2 bg-primary text-light" target="_blanck" href="mailto:' + email + '" id="modal-close">Envoyer par email</a>');
        modalContainerP.appendChild(customBoxP);
        document.body.appendChild(modalContainerP);

        document.getElementById('modal-close').addEventListener('click', async function() {
            modalClose();
        });

        async function modalClose() {
            while (modalContainerP.hasChildNodes()) {
                modalContainerP.removeChild(modalContainerP.firstChild);
            }
            document.body.removeChild(modalContainerP);
        };
    };
    /********* Response User Box *********/
    async function displayValidate(msg) {
        let modalContainerP = document.createElement('div');
        modalContainerP.setAttribute('id', 'modal');
        let customBoxP = document.createElement('div');
        customBoxP.className = 'custom-box text-start';
        customBoxP.innerHTML = '<p class="fs-6 text-primary text-center"><strong>' + msg + '</p></br>';
        customBoxP.innerHTML += (
            '</br><button class="btn my-1 mx-2 bg-primary text-light" id="modal-close">Ok</button>');
        modalContainerP.appendChild(customBoxP);
        document.body.appendChild(modalContainerP);

        document.getElementById('modal-close').addEventListener('click', async function() {
            modalClose();
        });

        async function modalClose() {
            while (modalContainerP.hasChildNodes()) {
                modalContainerP.removeChild(modalContainerP.firstChild);
            }
            document.body.removeChild(modalContainerP);
        };
    };
    /********* Add actuality *********/
    if (document.getElementById('addActuality')) {
        /********* Begin of box *********/
        let modalContainer = document.createElement('div');
        modalContainer.setAttribute('id', 'modal');
        let customBox = document.createElement('div');
        customBox.className = 'custom-box text-start';
        let btn_u = document.getElementById('addActuality');
        btn_u.addEventListener('click', box_actu);
        
        async function box_actu(){
            customBox.innerHTML = '<p class="fs-6 my-0 text-primary text-center"><strong>Ajouter une actualité</strong></p>';
            customBox.innerHTML += (
                'Titre* : </br><input type="text" id="ev-title" name="ev-title"></br>');
            customBox.innerHTML += (
                'Début : </br><input type="date" id="start" name="ev-start" value="2021-08-19" min="2021-08-19"></br>');
            customBox.innerHTML += (
                'Fin : </br><input type="date" id="end" name="ev-end" value="2021-08-19" min="2021-08-19"></br>');
            customBox.innerHTML += (
                '<textarea type="text" id="modal-prompt" name="ev-text" placeholder="**gras** *italique* #retour à la ligne">');
            customBox.innerHTML += (
                '</br>Photo (exemple: maphoto.png) : </br><input type="text" id="link" name="ev-link">');
            customBox.innerHTML += '</br><button class="btn my-1 mx-2 bg-primary text-light" id="modal-close">Annuler</button>';
            customBox.innerHTML += '<button class="btn my-1 bg-primary text-light" id="modal-submit">Envoyer</button>';
            modalShow();
        };

        async function modalShow() {
            modalContainer.appendChild(customBox);
            document.body.appendChild(modalContainer);
            document.getElementById('modal-close').addEventListener('click', async function() {
                modalClose();
            });
            if (document.getElementById('modal-submit')) {
                document.getElementById('modal-submit').addEventListener('click', async function () {
                    let formData = new FormData();
                    formData.append('title', document.getElementById('ev-title').value);
                    formData.append('start', document.getElementById('start').value);
                    formData.append('end', document.getElementById('end').value);
                    formData.append('article', document.getElementById('modal-prompt').value);
                    formData.append('link', document.getElementById('link').value);
                    formData.append('box', "actuality");
                    let request = new Request('add_data', {method: 'POST', body: formData});
                    fetch(request)
                    .then(result => {
                        return result.json() //Convert response to JSON
                    })
                    .then(data => {
                        modalClose();
                        if (data.resp == false) {
                            displayErrorBox("Erreur lors de l'ajout de l'actualité")
                        };
                        if (data.resp == true) {
                            displayValidate("Actualité ajouté")
                        }
                    })
                });
            };
        };

        async function modalClose() {
            while (modalContainer.hasChildNodes()) {
                modalContainer.removeChild(modalContainer.firstChild);
            }
            document.body.removeChild(modalContainer);
        };
    };

    /********* Add user *********/
    if (document.getElementById('addUser')) {
        let modalContainer = document.createElement('div');
        modalContainer.setAttribute('id', 'modal');
        let customBox = document.createElement('div');
        customBox.className = 'custom-box text-start';
        let btn_u = document.getElementById('addUser');
        btn_u.addEventListener('click', add_box_user);
        
        async function add_box_user(){
            customBox.innerHTML = '<p class="fs-6 my-0 text-primary text-center"><strong>Ajouter un étudiant</strong></p></br>';
            customBox.innerHTML += (
                'Nom : </br><input type="text" id="lastname" name="lastname"></br>');
            customBox.innerHTML += (
                'Prénom : </br><input type="text" id="firstname" name="firstname"></br>');
            customBox.innerHTML += (
                'Email : </br><input type="text" id="email" name="email"></br>');
            customBox.innerHTML += (
                'Confirmez l\'adresse Email : </br><input type="text" id="emailconfirm" name="emailconfirm"></br>');
            customBox.innerHTML += (
                'Staff : <input type="checkbox" id="staff" name="staff" class="col-lg-1"></br>');
            customBox.innerHTML += '</br><button class="btn my-1 mx-2 bg-primary text-light" id="modal-close">Annuler</button>';
            customBox.innerHTML += '<button class="btn my-1 bg-primary text-light" id="modal-submit">Envoyer</button>';
            modalShowUser();
        };

        async function modalShowUser() {
            modalContainer.appendChild(customBox);
            document.body.appendChild(modalContainer);
            document.getElementById('modal-close').addEventListener('click', async function() {
                modalClose();
            });
            if (document.getElementById('modal-submit')) {
                document.getElementById('modal-submit').addEventListener('click', async function () {
                    let formData = new FormData();
                    formData.append('lastname', document.getElementById('lastname').value)
                    formData.append('firstname', document.getElementById('firstname').value)
                    formData.append('email', document.getElementById('email').value)
                    formData.append('emailconfirm', document.getElementById('emailconfirm').value)
                    formData.append('staff', document.getElementById('staff').checked)
                    let request = new Request('add_user', {method: 'POST', body: formData});
                    fetch(request)
                    .then(result => {
                            return result.json() //Convert response to JSON
                    })
                    .then(data => {
                        modalClose();
                        if (data.resp == false) {
                            displayErrorBox(data.state)
                        };
                        if (data.resp == true) {
                            displayPasswordBox(data.id, data.password, data.email)
                        };
                    });
                    modalClose();
                });
            };
        };

        async function modalClose() {
            while (modalContainer.hasChildNodes()) {
                modalContainer.removeChild(modalContainer.firstChild);
            }
            document.body.removeChild(modalContainer);
        };
    };

    /********* FAQ *********/
    if (document.getElementById('addFaq')) {
        let modalContainer = document.createElement('div');
        modalContainer.setAttribute('id', 'modal');
        let customBox = document.createElement('div');
        customBox.className = 'custom-box text-start';
        let btn_u = document.getElementById('addFaq');
        btn_u.addEventListener('click', add_box_faq);
        
        async function add_box_faq(){
            customBox.innerHTML = '<p class="fs-6 my-0 text-primary"><strong>Ajouter une réponse à la F.A.Q</strong></p></br>';
            customBox.innerHTML += (
                'Question* : </br><input type="text" id="question" name="question"></br>');
            customBox.innerHTML += (
                'Réponse* : </br><p class="fs-7 my-0 text-primary text-center">Gras= **texte** | Italique= *texte* | Retour à la ligne= espaceX2</p>');
            customBox.innerHTML += (
                '<textarea type="text" id="modal-prompt" name="text">');
            customBox.innerHTML += '</br><button class="btn my-1 mx-2 bg-primary text-light" id="modal-close">Annuler</button>';
            customBox.innerHTML += '<button class="btn my-1 bg-primary text-light" id="modal-submit">Envoyer</button>';
            modalShowFaq();
        };

        async function modalShowFaq() {
            modalContainer.appendChild(customBox);
            document.body.appendChild(modalContainer);
            document.getElementById('modal-close').addEventListener('click', async function() {
                modalClose();
            });
            if (document.getElementById('modal-submit')) {
                document.getElementById('modal-submit').addEventListener('click', async function () {
                    alert('in fonc')
                    let formData = new FormData();
                    formData.append('question', document.getElementById('question').value)
                    formData.append('text', document.getElementById('modal-prompt').value)
                    formData.append('box', "faq")
                    let request = new Request('add_data', {method: 'POST', body: formData});
                    fetch(request)
                    .then(result => {
                        return result.json() //Convert response to JSON
                    })
                    .then(data => {
                        modalClose();
                        if (data.resp == false) {
                            displayErrorBox("Erreur lors de l'ajout de la question")
                        };
                        if (data.resp == true) {
                            displayValidate("Question ajoutée")
                        }
                    })
                });
            };
        };

        async function modalClose() {
            while (modalContainer.hasChildNodes()) {
                modalContainer.removeChild(modalContainer.firstChild);
            }
            document.body.removeChild(modalContainer);
        };
    };

    if (document.getElementById('addLink')) {
        let modalContainer = document.createElement('div');
        modalContainer.setAttribute('id', 'modal');
        let customBox = document.createElement('div');
        customBox.className = 'custom-box text-start';
        let btn_u = document.getElementById('addLink');
        btn_u.addEventListener('click', add_box_link);
        
        async function add_box_link(){
            customBox.innerHTML = '<p class="fs-6 text-primary"><strong>Ajouter un lien utile</strong></p></br>';
            customBox.innerHTML += (
                'Titre : </br><input type="text" id="title" name="title"></br>');
            customBox.innerHTML += (
                'Lien : </br><input type="text" id="link" name="link"></br>');
            customBox.innerHTML += '</br><button class="btn my-1 mx-2 bg-primary text-light" id="modal-close">Annuler</button>';
            customBox.innerHTML += '<button class="btn my-1 bg-primary text-light" id="modal-submit">Envoyer</button>';
            modalShowLink();
        };

        async function modalShowLink() {
            modalContainer.appendChild(customBox);
            document.body.appendChild(modalContainer);
            document.getElementById('modal-close').addEventListener('click', async function() {
                modalClose();
            });
            if (document.getElementById('modal-submit')) {
                document.getElementById('modal-submit').addEventListener('click', async function () {
                    let formData = new FormData();
                    formData.append('title', document.getElementById('title').value)
                    formData.append('link', document.getElementById('link').value)
                    formData.append('box', "link")
                    let request = new Request('add_data', {method: 'POST', body: formData});
                    fetch(request)
                    .then(result => {
                        return result.json() //Convert response to JSON
                    })
                    .then(data => {
                        modalClose();
                        if (data.resp == false) {
                            displayErrorBox("Erreur lors de l'ajout du lien")
                        };
                        if (data.resp == true) {
                            displayValidate("Lien ajouté")
                        }
                    })
                });
            };
        };

        async function modalClose() {
            while (modalContainer.hasChildNodes()) {
                modalContainer.removeChild(modalContainer.firstChild);
            }
            document.body.removeChild(modalContainer);
        };
    };
    if (document.getElementById('addTem')) {
        /********* Begin of alert box delete profil *********/
        let modalContainer = document.createElement('div');
        modalContainer.setAttribute('id', 'modal');
        let customBox = document.createElement('div');
        customBox.className = 'custom-box text-start';
        let btn_u = document.getElementById('addTem');
        btn_u.addEventListener('click', add_box_tem);
        
        async function add_box_tem(){
            customBox.innerHTML = '<p class="fs-6 my-0 text-primary"><strong>Ajouter un témoignage</strong></p></br>';
            customBox.innerHTML += (
                'Texte : </br><textarea type="text" id="modal-prompt" name="text">');
            customBox.innerHTML += (
                '</br>Témoin : </br><textarea type="text" id="modal-prompt1" name="author">');
            customBox.innerHTML += (
                '</br>Secteur : </br><form id="form-control"><select id="select">' +
                '<option>Avocature et Magistrature' +
                '<option>Secteur privé et public' + 
                '<option>Recherche' +
                '</select></form>');
            customBox.innerHTML += '</br><button class="btn my-1 mx-2 bg-primary text-light" id="modal-close">Annuler</button>';
            customBox.innerHTML += '<button class="btn my-1 bg-primary text-light" id="modal-submit">Envoyer</button>';
            modalShowTem();
        };

        async function modalShowTem() {
            modalContainer.appendChild(customBox);
            document.body.appendChild(modalContainer);
            document.getElementById('modal-close').addEventListener('click', async function() {
                modalClose();
            });
            if (document.getElementById('modal-submit')) {
                document.getElementById('modal-submit').addEventListener('click', async function () {
                    let formData = new FormData();
                    formData.append('text', document.getElementById('modal-prompt').value)
                    formData.append('author', document.getElementById('modal-prompt1').value)
                    formData.append('sector', document.getElementById('select').options[document.getElementById('select').selectedIndex].value)
                    formData.append('box', "testimony")
                    let request = new Request('add_data', {method: 'POST', body: formData});
                    fetch(request)
                    .then(result => {
                        return result.json() //Convert response to JSON
                    })
                    .then(data => {
                        modalClose();
                        if (data.resp == false) {
                            displayErrorBox("Erreur lors de l'ajout du Témoignage")
                        };
                        if (data.resp == true) {
                            displayValidate("Témoignage ajoutée")
                        }
                    })
                });
            };
        };

        async function modalClose() {
            while (modalContainer.hasChildNodes()) {
                modalContainer.removeChild(modalContainer.firstChild);
            }
            document.body.removeChild(modalContainer);
        };
    };
    if (document.getElementById('addPromo')) {
        /********* Begin of alert box delete profil *********/
        let modalContainer = document.createElement('div');
        modalContainer.setAttribute('id', 'modal');
        let customBox = document.createElement('div');
        customBox.className = 'custom-box text-start';
        let btn_u = document.getElementById('addPromo');
        btn_u.addEventListener('click', add_box_prom);
        
        async function add_box_prom(){
            customBox.innerHTML = '<p class="fs-6 text-primary"><strong>Ajouter une promotion</strong></p></br>';
            customBox.innerHTML += (
                'Bannière (exemple : "Promotion 2021 - 2022") : </br><input type="text" id="title" name="title">');
            customBox.innerHTML += (
                '</br>Descriptif : </br><textarea type="text" id="modal-prompt" name="description">');
            customBox.innerHTML += (
                '</br>Photo (exemple: maphoto.png) : </br><input type="text" id="img_title" name="img_title"></br>');
            customBox.innerHTML += '</br><button class="btn my-1 mx-2 bg-primary text-light" id="modal-close">Annuler</button>';
            customBox.innerHTML += '<button class="btn my-1 bg-primary text-light" id="modal-submit">Envoyer</button>';
            modalShowProm();
        };

        async function modalShowProm() {
            modalContainer.appendChild(customBox);
            document.body.appendChild(modalContainer);
            document.getElementById('modal-close').addEventListener('click', async function() {
                modalClose();
            });
            if (document.getElementById('modal-submit')) {
                document.getElementById('modal-submit').addEventListener('click', async function () {
                    let formData = new FormData();
                    formData.append('title', document.getElementById('title').value)
                    formData.append('description', document.getElementById('modal-prompt').value)
                    formData.append('img_title', document.getElementById('img_title').value)
                    formData.append('box', "promotion")
                    let request = new Request('add_data', {method: 'POST', body: formData});
                    fetch(request)
                    .then(result => {
                        return result.json() //Convert response to JSON
                    })
                    .then(data => {
                        modalClose();
                        if (data.resp == false) {
                            displayErrorBox("Erreur lors de l'ajout de la promotion")
                        };
                        if (data.resp == true) {
                            displayValidate("Promotion ajoutée")
                        }
                    })
                });
            };
        };

        async function modalClose() {
            while (modalContainer.hasChildNodes()) {
                modalContainer.removeChild(modalContainer.firstChild);
            }
            document.body.removeChild(modalContainer);
        };
    };
});