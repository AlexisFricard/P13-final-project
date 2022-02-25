document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('form-promotion')) {
        let btnStep2 = document.getElementById('btn-step-2')
        let btnStep3 = document.getElementById('btn-step-3')
        let btnStep3back = document.getElementById('btn-step-3-b')
        let btnStep4 = document.getElementById('btn-step-4')
        let btnStep4back = document.getElementById('btn-step-4-b')
        let btnStep5back = document.getElementById('btn-step-5-b')
        let btnback = document.getElementById('btn-back')

        btnStep2.addEventListener('click', function() {
            btnback.setAttribute('style', "display:block")
            document.getElementById('form-promotion').setAttribute('style' ,"display: none;")
            document.getElementById('form-colonne-1').setAttribute('style' ,"display: inline;")
            document.getElementById('ul-promo-1').setAttribute("style", "color:rgba(54, 54, 54, 0.082)")
            document.getElementById('ul-promo-2').setAttribute("style", "color:rgb(54, 54, 54)")
        })
        btnStep3.addEventListener('click', function() {
            document.getElementById('form-colonne-1').setAttribute('style' ,"display: none;")
            document.getElementById('form-colonne-2').setAttribute('style' ,"display: inline;")
            document.getElementById('ul-promo-2').setAttribute("style", "color:rgba(54, 54, 54, 0.082)")
            document.getElementById('ul-promo-3').setAttribute("style", "color:rgb(54, 54, 54)")
        })
        btnStep3back.addEventListener('click', function() {
            document.getElementById('form-promotion').setAttribute('style' ,"display: inline;")
            document.getElementById('form-colonne-1').setAttribute('style' ,"display: none;")
            document.getElementById('ul-promo-1').setAttribute("style", "color:rgb(54, 54, 54)")
            document.getElementById('ul-promo-2').setAttribute("style", "color:rgba(54, 54, 54, 0.082)")
        })
        btnStep4.addEventListener('click', function() {
            document.getElementById('form-colonne-2').setAttribute('style' ,"display: none;")
            document.getElementById('form-colonne-3').setAttribute('style' ,"display: inline;")
            document.getElementById('ul-promo-3').setAttribute("style", "color:rgba(54, 54, 54, 0.082)")
            document.getElementById('ul-promo-4').setAttribute("style", "color:rgb(54, 54, 54)")
        })
        btnStep4back.addEventListener('click', function() {
            document.getElementById('form-colonne-1').setAttribute('style' ,"display: inline;")
            document.getElementById('form-colonne-2').setAttribute('style' ,"display: none;")
            document.getElementById('ul-promo-2').setAttribute("style", "color:rgb(54, 54, 54)")
            document.getElementById('ul-promo-3').setAttribute("style", "color:rgba(54, 54, 54, 0.082)")
        })
        btnStep5back.addEventListener('click', function() {
            document.getElementById('form-colonne-2').setAttribute('style' ,"display: inline;")
            document.getElementById('form-colonne-3').setAttribute('style' ,"display: none;")
            document.getElementById('ul-promo-3').setAttribute("style", "color:rgb(54, 54, 54)")
            document.getElementById('ul-promo-4').setAttribute("style", "color:rgb(54, 54, 54, 0.082)")
        })
    }
    if (document.getElementById('add_utilisateur')) {
        let btnback = document.getElementById('btn-back')
        let list_of_button = ['utilisateur', 'FAQ', 'lien', 'photo', 'promotion', 'actualité', 'témoignage', 'member']

        let btnOptUser = document.getElementById('opt_user')
        let btnOptFAQ = document.getElementById('opt_FAQ')
        let btnOptPhoto = document.getElementById('opt_photo')
        let btnOptLink = document.getElementById('opt_lien')
        let btnOptTestimony = document.getElementById('opt_témoignage')
        let btnOptActu = document.getElementById('opt_actualité')
        let btnOptMember = document.getElementById('opt_member')
        let btnOptTeam = document.getElementById('opt_member_team')
        let btnOptOffice = document.getElementById('opt_member_office')

        let btnAddUser = document.getElementById('add_utilisateur')
        let btnAddFAQ = document.getElementById('add_FAQ')
        let btnAddlien = document.getElementById('add_lien')
        let btnAddphoto = document.getElementById('add_photo')
        let btnAddpromotion = document.getElementById('add_promotion')
        let btnAddactualité = document.getElementById('add_actualité')
        let btnAddTemoignage = document.getElementById('add_temoignage')
        let btnAddTeam = document.getElementById('add_member_team')
        let btnAddOffice = document.getElementById('add_member_office')

        // USER
        btnOptUser.addEventListener("click", function() {
            btnback.setAttribute('style', "display:block");
            disable_all_expect('utilisateur', 1);
            disable_all_expect('opts-utilisateur', 1);
            document.getElementById('utilisateur').setAttribute('style', 'display:none');
        });
        btnAddUser.addEventListener('click', function() {
            btnback.setAttribute('style', "display:block")
            disable_all_expect('utilisateur', 1);
            document.getElementById('opts-utilisateur').setAttribute('style', 'display:none');
        });

        // FAQ
        btnOptFAQ.addEventListener("click", function() {
            btnback.setAttribute('style', "display:block");
            disable_all_expect('FAQ', 1);
            disable_all_expect('opts-FAQ', 1);
            document.getElementById('FAQ').setAttribute('style', 'display:none');
        });
        btnAddFAQ.addEventListener('click', function() {
            btnback.setAttribute('style', "display:block")
            disable_all_expect('FAQ', 1);
            document.getElementById('opts-FAQ').setAttribute('style', 'display:none');
        });

        // LINKS
        btnAddlien.addEventListener('click', function() {
            btnback.setAttribute('style', "display:block")
            disable_all_expect('lien', 1);
            document.getElementById('opts-lien').setAttribute('style', 'display:none');
        });
        btnOptLink.addEventListener("click", function() {
            btnback.setAttribute('style', "display:block");
            disable_all_expect('lien', 1);
            disable_all_expect('opts-lien', 1);
            document.getElementById('lien').setAttribute('style', 'display:none');
        });

        // PHOTOS
        btnAddphoto.addEventListener('click', function() {
            btnback.setAttribute('style', "display:block")
            disable_all_expect('photo', 1);
            document.getElementById('opts-photo').setAttribute('style', 'display:none');
        });
        btnOptPhoto.addEventListener("click", function() {
            btnback.setAttribute('style', "display:block");
            disable_all_expect('photo', 1);
            disable_all_expect('opts-photo', 1);
            document.getElementById('photo').setAttribute('style', 'display:none');
        });

        // PROMOTIONS
        btnAddpromotion.addEventListener('click', function() {
            btnback.setAttribute('style', "display:block")
            disable_all_expect('promotion', 1);
            document.getElementById('ul-promo').setAttribute('style', 'text-align:start;display:block')
        });

        // ACTUALITY
        btnOptActu.addEventListener("click", function() {
            btnback.setAttribute('style', "display:block");
            disable_all_expect('actualité', 1);
            disable_all_expect('opts-actualité', 1);
            document.getElementById('actualité').setAttribute('style', 'display:none');
        });
        btnAddactualité.addEventListener('click', function() {
            btnback.setAttribute('style', "display:block")
            disable_all_expect('actualité', 1);
            document.getElementById('opts-actualité').setAttribute('style', 'display:none');
        });

        // TESTIMONY
        btnOptTestimony.addEventListener("click", function() {
            btnback.setAttribute('style', "display:block");
            disable_all_expect('témoignage', 1);
            disable_all_expect('opts-témoignage', 1);
            document.getElementById('témoignage').setAttribute('style', 'display:none');
        });
        btnAddTemoignage.addEventListener('click', function() {
            btnback.setAttribute('style', "display:block")
            disable_all_expect('témoignage', 1);
            document.getElementById('opts-témoignage').setAttribute('style', 'display:none');
        });
    
        // Member
        btnOptMember.addEventListener("click", function() {
            btnback.setAttribute('style', "display:block");
            disable_all_expect('opts-member', 1);
        });
        // Member - Team
        btnOptTeam.addEventListener('click', function() {
            btnback.setAttribute('style', "display:block")
            disable_all_expect('member_team', 0);
            document.getElementById('opts-member').setAttribute('style', 'display:none');
        });
        btnAddTeam.addEventListener('click', function() {
            btnback.setAttribute('style', "display:block")
            disable_all_expect('form_member_team', 0);
            document.getElementById('member_team').setAttribute('style', 'display:none');
        });
        // Member - Office
        btnOptOffice.addEventListener('click', function() {
            btnback.setAttribute('style', "display:block")
            disable_all_expect('member_office', 0);
            document.getElementById('opts-member').setAttribute('style', 'display:none');
        });
        btnAddOffice.addEventListener('click', function() {
            btnback.setAttribute('style', "display:block")
            disable_all_expect('form_member_office', 0);
            document.getElementById('member_office').setAttribute('style', 'display:none');
        });

        // FUNCTION
        async function disable_all_expect(div, b) {
            for (let division of list_of_button) {
                if (b == 1) {
                    if (div != division) {
                        let division_ = "b-" + division;
                        let disable_it = document.getElementById(division_);
                        disable_it.setAttribute('style', 'display:none;')
                    };
                };
                let form = document.getElementById(div);
                form.setAttribute('style', 'display:block;')
            };
        };
    };
});