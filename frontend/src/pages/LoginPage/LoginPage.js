import React, {useState} from 'react';
import {useForm} from "react-hook-form";
import {useNavigate} from "react-router-dom";

import {authService} from "../../services";

const LoginPage = () => {
    const {register, handleSubmit} = useForm();
    const [error, setError] = useState(null);
    const navigate = useNavigate();

    const login = async (userCredential) => {
        try {
            await authService.login(userCredential);
            navigate('/profile')

        } catch (e) {
            if (e.response.status === 401) {
                setError(e.response.data)
            }
        }
    }

    return (
        <div>
            LoginPage
            <div>
                <form onSubmit={handleSubmit(login)}>
                    <input type="text" placeholder={'email'} {...register('email')}/>
                    <input type="text" placeholder={'password'} {...register('password')}/>
                    <button>Login</button>
                </form>
            </div>
            {error?.detail &&
                <div>
                    {error.detail}
                </div>
            }
        </div>
    );
};

export {LoginPage};