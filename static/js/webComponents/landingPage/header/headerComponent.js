class headerLandingPageComponent extends HTMLElement {
    constructor () {
        super ();

        this.shadow = this.attachShadow({mode:"open"});
        this.shadow.append(this.headerTemplate)
    }

    get headerTemplate () {
        const headerDiv = document.createElement("header");

        headerDiv.innerHTML = `
        
            <style>
                @import url("/static/css/components/landingPage/header.css");
            </style>

            <div class="header_logo">
            </div>

            <nav class="header_navigation">
                <a href="" class="header_navigation-a">
                    Home
                </a>
                <a href="" class="header_navigation-a">
                    Files on mc
                </a>
                <a href="" class="header_navigation-a">
                    Features
                </a>
            </nav>

            <nav class="header_user">
                <a href="/user/login/" class="header_user-a">
                    <slot name="loginImage"></slot>
                    <img src="{% static 'images/user.png' %}" alt="">
                    Login
                </a>
            </nav>

        `

        return headerDiv
    }
}

export default headerLandingPageComponent