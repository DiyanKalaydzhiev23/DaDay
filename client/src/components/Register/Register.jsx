import { useForm } from 'react-hook-form';
import { useNavigate } from 'react-router';
import { authService } from '../../services/authService';

const Register = () => {
    const { register, formState: { errors }, handleSubmit } = useForm({ mode: 'onSubmit', reValidateMode: 'onChange' });
    const navigate = useNavigate();
    
    const registerUser = (data) => {
        authService.register(data)
            .then(() => {
                navigate('/');
            })
            .catch(err => {
                console.log(err);
            });
    }

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
                    <label htmlFor="confirm-password">Password</label>
                    <input type="password" name="confirmPassword" id="confirm-password" {...register('repeatPassword', { required: {value: true, message: 'Repeat password is required!'}})}  className="form-input"/>
                    {errors.confirmPassword && <p>{errors.confirmPassword.message}</p>}
                </article>

                <article className="input-group">
                    <label htmlFor="avatar">Avatar</label>
                    <input {...register('avatar', { required: {value: true, message: 'Avatar is required!'}})} type="number" name="avatar" id="avatar"  className="form-input"/>
                    {errors.avatar && <p>{errors.avatar.message}</p>}
                </article>

                <article className="input-group">
                    <input type="submit" value="Register" />
                </article>
            </form>
        </section>
    );
}

export default Register;