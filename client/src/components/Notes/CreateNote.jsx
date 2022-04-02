import { useEffect } from "react";
import { useState } from "react";
import { notesService } from "../../services/notesService";

const CreateNote = () => {
    const [question, setQuestion] = useState(null);
    const user = localStorage.getItem('user') ? JSON.parse(localStorage.getItem('user')) : null;

    useEffect(() => {
        notesService.getOne(user)
            .then(response => {

                console.log(response);
            })
    }, [user.user_id]);
    return (
        <section>
            <h1>CreateNote page</h1>

            <p>{question}</p>

        </section>
    );
}

export default CreateNote;