import headerLandingPageComponent from "/static/js/webComponents/landingPage/header/headerComponent.js"


window.onload = () => {
    customElements.define("header-component", headerLandingPageComponent)
}