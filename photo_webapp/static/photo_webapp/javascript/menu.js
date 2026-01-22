const page = document.body.dataset.page;

if(page === 'photo_gallery'){
    if(!document.getElementById("photo_gallery_menu_link").classList.contains('active')){
        document.getElementById("photo_gallery_menu_link").classList.add('active');
    }
    document.getElementById("contact_form_menu_link").classList.remove('active');
} else if(page === 'contact_form'){
        document.getElementById("contact_form_menu_link").classList.add('active');
        document.getElementById("photo_gallery_menu_link").classList.remove('active');
}