class porcentageBar extends HTMLElement {
    constructor () {
        super ()

        this.shadow = this.attachShadow({mode:"open"})
        this.shadow.append(this.porcentageBarTemplate)
    }

    connectedCallback () {
        let total = this.getAttribute("totalStorage")
        let type_used_storage = this.getAttribute("type_storage")

        let porcentage = ((type_used_storage / total) * 100).toFixed(2)

        let porcentage_bar =this.shadow.querySelector(".content_area_types_cards_card_space_actualSpaceSpace")

        porcentage_bar.style.width = `${porcentage}%`
    }

    get porcentageBarTemplate () {
        const porcentageBarDiv = document.createElement("div")
        porcentageBarDiv.classList.add("content_area_types_cards_card_space_actualSpaceSpace")
        porcentageBarDiv.innerHTML = `
        
        <style>
            .content_area_types_cards_card_space_actualSpaceSpace{
                width: 10%;
                border-radius: 10px;
                height: 10px;
                background-color: var(--dark-purple);
            }
        
        </style>

        `

        return porcentageBarDiv
    }
}

customElements.define("porcentage-bar", porcentageBar)