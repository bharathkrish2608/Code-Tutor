const API_URL = import.meta.env.VITE_API_URL || 'https://code-tutor-m4di.onrender.com/api';


export const analyzeCode = async (code) => {
    try {
        const response = await fetch(`${API_URL}/analyze/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ code }),
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'Failed to analyze code. Please check your API key and try again.');
        }

        return data.result;
    } catch (error) {
        if (error.message === 'Failed to fetch') {
            throw new Error('Could not connect to the backend server. Is it running?');
        }
        throw error;
    }
};
