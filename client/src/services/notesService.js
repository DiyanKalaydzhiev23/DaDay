import { baseUrl } from "../constants";

const getReport = async (userId) => {
    const response = await fetch(`${baseUrl}/notes/${userId}`);
    const data = await response.json();

    if (!response.ok) {
        throw new Error(data);
    }

    // [
    //     { id: 1, desc: 'I felt sad', emotion: 2, date: '2022-02-10' },
    //     { id: 2, desc: 'I felt happy', emotion: 5, date: '2022-01-23' }
    // ]
    return data;
}

const getOne = async (user) => {
    const response = await fetch(`${baseUrl}/share-day/${user.user_id}`, {
        headers: { 
            'Content-Type': 'application/json'
        }
    });
    const data = await response.json();

    if (!response.ok) {
        throw new Error(data);
    }

    return data;
}

export const notesService = { getReport, getOne };