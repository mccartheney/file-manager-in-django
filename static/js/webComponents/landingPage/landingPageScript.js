import welcomeComponent from "/static/js/webComponents/landingPage/welcome/welcomeComponent.js"
import headerLandingPageComponent from "/static/js/webComponents/landingPage/header/headerComponent.js"
import filesOnMcComponent from "/static/js/webComponents/landingPage/filesOnMc/fileOnMcComponent.js"
import logoComponent from "/static/js/webComponents/logo/logoComponent.js"


window.onload = () => {
    customElements.define("header-component", headerLandingPageComponent)
    customElements.define("welcome-component", welcomeComponent)
    customElements.define("files-on-mc-component", filesOnMcComponent)
    customElements.define("logo-component", logoComponent)
}