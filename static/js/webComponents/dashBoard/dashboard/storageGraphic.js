class storageGraphic extends HTMLElement {
    constructor (){
        super()

        this.shadow = this.attachShadow({mode:"open"})
        this.shadow.append(this.storageGraphicTemplate)
    }

    connectedCallback () {
        window.onload = () => {
            const data = {
                'Images': this.getAttribute("imagesPorcentage"),
                'Videos': this.getAttribute("videosPorcentage"),
                'Audios': this.getAttribute("audiosPorcentage"),
                'Documents': this.getAttribute("documentsPorcentage")
            };
            const maxValue = 50; // Maximum value for the chart

            const chart = this.shadow.getElementById('chart');
            const yAxis = this.shadow.getElementById('y-axis');

            // Calculate the number of labels needed based on the chart height and step size
            const chartHeight = chart.offsetHeight;
            const stepSize = 10; // Adjust step size as needed
            const numberOfLabels = Math.ceil(maxValue / stepSize);

            yAxis.style.gridTemplateRows = `repeat(${numberOfLabels}, 1fr)`;

            // Create Y-axis labels from highest to lowest
            for (let i = numberOfLabels; i >= 0; i--) {
                const yAxisLabel = document.createElement('div');
                yAxisLabel.classList.add('y-axis-label');
                yAxisLabel.textContent = (i * stepSize) + ' MB';
                yAxis.appendChild(yAxisLabel);
            }

            // Create bars
            for (let key in data) {
                console.log(key);
                const value = data[key];
                const heightPercent = (value / maxValue) * 100;

                const bar = document.createElement('div');
                bar.classList.add('bar');

                
                const barContent = document.createElement('div');
                barContent.style.height = heightPercent + '%';
                
                if (key == "Images") {
                    barContent.style.backgroundColor = "#00d73c"
                }else if (key == "Videos") {
                    barContent.style.backgroundColor = "#610b96"
                } else if (key == "Audios") {
                    barContent.style.backgroundColor = "#d71925"
                } else if (key == "Documents") {
                    barContent.style.backgroundColor = "#177bab"
                }

                const barLabel = document.createElement('div');
                barLabel.classList.add('bar-label');
                barLabel.textContent = key;
                barLabel.style.background = "transparent"

                bar.appendChild(barLabel);
                bar.appendChild(barContent);
                chart.appendChild(bar);
            }
        };
    }


    get storageGraphicTemplate () {
        const storageGraphicDiv = document.createElement("div")
        storageGraphicDiv.setAttribute("id","chart-container")

        storageGraphicDiv.innerHTML = `
            <style>
                @import url('/static/css/components/dashboard/storageGraphic.css')            
            </style>

            <div id="y-axis"></div>
            <div id="chart"></div>
        `

        return storageGraphicDiv
    }
}

customElements.define("storage-graphic",storageGraphic)
