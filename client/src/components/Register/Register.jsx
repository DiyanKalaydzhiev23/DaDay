import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { useNavigate } from 'react-router';
import { authService } from '../../services/authService';

import './Register.css';

const Register = () => {
    const { register, formState: { errors }, handleSubmit } = useForm({ mode: 'onSubmit', reValidateMode: 'onChange' });
    const navigate = useNavigate();

    const [avatar, setAvatar] = useState(null);
    
    const registerUser = (data) => {
        authService.register(data, avatar)
            .then(() => {
                navigate('/');
            })
            .catch(err => {
                console.log(err);
            });
    }

    const changeSrcToGif = (event) => {
        event.target.setAttribute('src', 'https://res.cloudinary.com/drinka/image/upload/v1648968348/da-day/cat-animation_gyamxz.gif');
    }

    const changeSrcToPng = (event) => event.target.setAttribute('src', '');

    return (
        <section className="flex flex-col items-center">
            <h1 className="title">Register</h1>

            <form onSubmit={handleSubmit(registerUser)}>
                <article className="input-group">
                    <label htmlFor="username">Username</label>
                    <input type="username" name="username" id="username" {...register('username', { required: { value: true, message: 'Usernmae is required!' } })}  className="form-input"/>
                    {errors.username && <p>{errors.username.message}</p>}
                </article>
                
                <article className="input-group">
                    <label htmlFor="email">Parent Email</label>
                    <input type="email" name="parentEmail" id="email" {...register('parentEmail', { required: { value: true, message: 'Email is required!' } })}  className="form-input"/>
                    {errors.email && <p>{errors.email.message}</p>}
                </article>

                <article className="input-group">
                    <label htmlFor="password">Password</label>
                    <input type="password" name="password" id="password" {...register('password', { required: {value: true, message: 'Password is required!'}})} className="form-input"/>
                    {errors.password && <p>{errors.password.message}</p>}
                </article>
                
                <article className="input-group">
                    <label htmlFor="confirm-password">Confirm Password</label>
                    <input type="password" name="confirmPassword" id="confirm-password" {...register('repeatPassword', { required: {value: true, message: 'Repeat password is required!'}})}  className="form-input"/>
                    {errors.confirmPassword && <p>{errors.confirmPassword.message}</p>}
                </article>

                <article className="input-group">
                    <label htmlFor="avatar">Avatar</label>
                    <section className="flex">
                        <article className="flex flex-col items-center">
                            <img src="https://res.cloudinary.com/drinka/image/upload/v1648973958/da-day/cat/cat-main_zs3bru.png" alt="Cat" onMouseOver={(e) => changeSrcToGif(e)} onMouseLeave={(e) => changeSrcToPng(e)} onClick={() => setAvatar(1)} className="avatar"/>
                        </article>

                        <article className="flex flex-col items-center">
                            <img src="https://res.cloudinary.com/drinka/image/upload/v1648973984/da-day/duck/duck-main_nz3pab.png" alt="Duck" onMouseOver={(e) => changeSrcToGif(e)} onMouseLeave={(e) => changeSrcToPng(e)} onClick={() => setAvatar(2)} className="avatar"/>
                        </article>
                    </section>
                </article>

                <article className="input-group">
                    <input type="submit" value="Register" />
                </article>
            </form>
        </section>
    );
}

export default Register;