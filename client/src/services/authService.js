import { baseUrl } from "../constants";

const register = async (data) => {
    if (data.password != data.repeatPassword) {
        throw new Error('Passwords must match!');
    }


    const reqBody = { 
        username: data.username, 
        password: data.password, 
        profile: { parent_email: data.parentEmail, avatar: Number(data.avatar) }
    };

    const response = await fetch(`${baseUrl}/auth/register/`, {
        method: 'POST',
        body: JSON.stringify(reqBody),
        headers: {
            'Content-Type': 'application/json'
        }
    });

    const responseData = await response.json();
    localStorage.setItem('username', data.username);
    localStorage.setItem('token', responseData.token);

    if (!response.ok) {
        throw new Error(responseData);
    }

    return responseData;
}

const login = async (data) => {
    const response = await fetch(`${baseUrl}/api-auth/`, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        }
    });

    const responseData = await data.json();

    if (!response.ok) {
        throw new Error(responseData);
    }

    return responseData;
}

export const authService = { register, login };