document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('form-promotion')) {
        let btnStep2 = document.getElementById('btn-step-2')
        let btnStep3 = document.getElementById('btn-step-3')
        let btnStep3back = document.getElementById('btn-step-3-b')
        let btnStep4 = document.getElementById('btn-step-4')
        let btnStep4back = document.getElementById('btn-step-4-b')
        let btnStep5back = document.getElementById('btn-step-5-b')

        btnStep2.addEventListener('click', function() {
            document.getElementById('form-promotion').setAttribute('style' ,"display: none;")
            document.getElementById('form-colonne-1').setAttribute('style' ,"display: inline;")
        })
        btnStep3.addEventListener('click', function() {
            document.getElementById('form-colonne-1').setAttribute('style' ,"display: none;")
            document.getElementById('form-colonne-2').setAttribute('style' ,"display: inline;")
        })
        btnStep3back.addEventListener('click', function() {
            document.getElementById('form-promotion').setAttribute('style' ,"display: inline;")
            document.getElementById('form-colonne-1').setAttribute('style' ,"display: none;")
        })
        btnStep4.addEventListener('click', function() {
            document.getElementById('form-colonne-2').setAttribute('style' ,"display: none;")
            document.getElementById('form-colonne-3').setAttribute('style' ,"display: inline;")
        })
        btnStep4back.addEventListener('click', function() {
            document.getElementById('form-colonne-1').setAttribute('style' ,"display: inline;")
            document.getElementById('form-colonne-2').setAttribute('style' ,"display: none;")
        })
        btnStep5back.addEventListener('click', function() {
            document.getElementById('form-colonne-2').setAttribute('style' ,"display: inline;")
            document.getElementById('form-colonne-3').setAttribute('style' ,"display: none;")
        })
    }
    if (document.getElementById('dashboard')) {
        let list_of_div = ["user", "faq", "link", "photo", "promo", "actu", "testi", "member"];

        let btnGoToPhoto = document.getElementById('btn_add_photo');

        let btnManUser = document.getElementById('man_user');
        let btnManFaq = document.getElementById('man_faq');
        let btnManLink = document.getElementById('man_link');
        let btnManPhoto = document.getElementById('man_photo');
        let btnManPromo = document.getElementById('man_promo');
        let btnManActu = document.getElementById('man_actu');
        let btnManTesti = document.getElementById('man_testi');
        let btnManMemb = document.getElementById('man_member');

        let btnOptOffice = document.getElementById('opt_member_office')
        let btnOptPedag = document.getElementById('opt_member_team')

        btnGoToPhoto.addEventListener('click', function() {
            document.getElementById('mod_member_team').setAttribute('style' ,"display: none;");
            btnManPhoto.click();
        })

        btnManUser.addEventListener('click', function() {
            document.getElementById('mod_member_team').setAttribute('style' ,"display: none;");
            display_it('user');
        })

        btnManFaq.addEventListener('click', function() {
            document.getElementById('mod_member_team').setAttribute('style' ,"display: none;");
            display_it('faq');
        })

        btnManLink.addEventListener('click', function() {
            document.getElementById('mod_member_team').setAttribute('style' ,"display: none;");
            display_it('link');
        })

        btnManPhoto.addEventListener('click', function() {
            document.getElementById('mod_member_team').setAttribute('style' ,"display: none;");
            display_it('photo');
        })

        btnManPromo.addEventListener('click', function() {
            document.getElementById('mod_member_team').setAttribute('style' ,"display: none;");
            display_it('promo');
        })

        btnManActu.addEventListener('click', function() {
            document.getElementById('mod_member_team').setAttribute('style' ,"display: none;");
            display_it('actu');
        })

        btnManTesti.addEventListener('click', function() {
            document.getElementById('mod_member_team').setAttribute('style' ,"display: none;");
            display_it('testi');
        })

        btnManMemb.addEventListener('click', function() {
            document.getElementById('div_member_1').setAttribute('style' ,"display: block;");
            document.getElementById('team_office').setAttribute('style' ,"display: none;")
            document.getElementById('team_pedag').setAttribute('style' ,"display: none;")
            document.getElementById('mod_member_team').setAttribute('style' ,"display: none;");
            display_it('member');
        })

        btnOptOffice.addEventListener('click', function() {
            document.getElementById('div_member_1').setAttribute('style' ,"display: none;");
            document.getElementById('team_office').setAttribute('style' ,"display: block;");
        })

        btnOptPedag.addEventListener('click', function() {
            document.getElementById('div_member_1').setAttribute('style' ,"display: none;");
            document.getElementById('team_pedag').setAttribute('style' ,"display: block;");
            document.getElementById('mod_member_team').setAttribute('style' ,"position: relative;left:19px;display: block;");
        })

        // FUNCTION
        async function display_it(div) {

            document.getElementById('div_home').setAttribute('style' ,"display: none;")
            div_name = "div_" + div

            for (let division of list_of_div) {
                if (div != division) {

                    del_name = "div_" + division;
                    let disable_it = document.getElementById(del_name);

                    disable_it.setAttribute('style', 'display:none;');
                };
            };
            document.getElementById(div_name).setAttribute('style' ,"height:100%;margin-left: 310px;display:block;");
        };
    };
});