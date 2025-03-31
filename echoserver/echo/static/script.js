const toMain = () => {
    window.location.href = "http://127.0.0.1:8000";
};

const toAdd = () => {
    window.open("http://127.0.0.1:8000/add/", '_blank');
};


const selectLimit = (event, page) => {

    let selectedLimit = event.target.value;
    console.log(event.target.value);
    page = 1;
    window.location.href = `http://127.0.0.1:8000/limit=${selectedLimit}/page=${page}`;
};


const selectPage = (event, limit) => {
    let selectedPage = event.target.textContent;
    window.location.href = `http://127.0.0.1:8000/limit=${limit}/page=${selectedPage}`;
};
