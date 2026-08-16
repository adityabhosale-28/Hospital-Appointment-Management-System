const BASE_URL = 'http://127.0.0.1:8000/api';

const api = {
    getToken: () => localStorage.getItem('token'),
    getRole: () => localStorage.getItem('role'),
    getUser: () => JSON.parse(localStorage.getItem('user') || '{}'),

    setSession: (data) => {
        localStorage.setItem('token', data.token);
        localStorage.setItem('role', data.role);
        localStorage.setItem('user', JSON.stringify(data.user));
    },

    clearSession: () => {
        localStorage.removeItem('token');
        localStorage.removeItem('role');
        localStorage.removeItem('user');
    },

    request: async (endpoint, method = 'GET', body = null) => {
        const headers = {
            'Content-Type': 'application/json'
        };
        const token = api.getToken();
        if (token) headers['Authorization'] = `Bearer ${token}`;

        const options = { method, headers };
        if (body) options.body = JSON.stringify(body);

        try {
            const res = await fetch(`${BASE_URL}${endpoint}`, options);
            const data = await res.json();
            if (!res.ok) {
                // FastAPI uses 'detail' for errors
                const errMsg = typeof data.detail === 'string' ? data.detail : (data.message || 'Something went wrong');
                throw new Error(errMsg);
            }
            return data;
        } catch (err) {
            alert(err.message);
            throw err;
        }
    },

    logout: () => {
        api.clearSession();
        window.location.href = 'login.html';
    },

    checkAuth: (requiredRole) => {
        const token = api.getToken();
        const role = api.getRole();
        if (!token) window.location.href = 'login.html';
        if (requiredRole && role !== requiredRole) {
            alert("Unauthorized access!");
            window.location.href = 'login.html';
        }
    }
};
