// See bottom for module exports

const BASE_URL = '/api';

function getGroups() {
    return fetch(`${BASE_URL}/groups`)
    .then(res => res.json())
}

module.exports = {
    groups: {
        list: getGroups
    }
}