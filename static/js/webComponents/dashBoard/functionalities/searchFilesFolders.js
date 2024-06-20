const allFolders = document.querySelectorAll("folder-component")
const allFiles = document.querySelectorAll("file-component")

let allComponents = []
let filteredComponents = []

const searchInput = document.querySelector(".content_area_fileManagement_search-input")
const folderAndFilesDiv = document.querySelector(".content_area_fileManagement_manager_title_folders")


allFolders.forEach(folder => {
    allComponents.push(folder)
});

allFiles.forEach(file => {
    allComponents.push(file)
});

const filterFilesOrFolders = (component, nameAttribute, searchQuery) => {
    if (nameAttribute) {
        if (nameAttribute.includes(searchQuery)) {
            filteredComponents.push(component)
        }
    }
}

const searchFilesAndFolders = (filesAndFolders, searchQuery) => {
    filteredComponents = []

    filesAndFolders.forEach(component => {
        const folderName = component.getAttribute("folderTitle")
        const fileName = component.getAttribute("fileTitle")

        filterFilesOrFolders(component, folderName, searchQuery)
        filterFilesOrFolders(component, fileName, searchQuery)
    })

    folderAndFilesDiv.innerHTML = ""

    filteredComponents.forEach(component => {
        folderAndFilesDiv.appendChild(component)
    })
}

const resetFolderAndFiles = (filesAndFolders) => {
    folderAndFilesDiv.innerHTML = ""
    allComponents.forEach(component => {
        folderAndFilesDiv.appendChild(component)
    })
}

searchInput.addEventListener("input", () => {
    let searchInputValue = searchInput.value

    if (searchInputValue != "") {
        searchFilesAndFolders(allComponents, searchInputValue)
    }else {
        console.log("reset components");
        resetFolderAndFiles(allComponents)
    }

})
