import { useState, useEffect } from "react";
import {notesService} from '../../../services/notesService';
import { formatDate } from "../../../utils";
import { Link } from "react-router-dom";

import './AllNotes.css';

const AllNotes = () => {
    const [notes, setNotes] = useState([]);
    const user = localStorage.getItem('user') ? JSON.parse(localStorage.getItem('user')) : null;

    useEffect(() => {
        notesService.getReport(user.user_id)
            .then((response) => {

                setNotes(response.map(obj => { 
                    return { id: obj.id, description: obj.description, date: formatDate(obj.date)};
                }));
            })
            .catch(err => {
                console.log(err);
            });
    });


    return (
        <section className="allNotes">
            {notes.map((note, i) => 
                <article className="note" key={i}>
                <p>
                    {note.description}
                </p>

                <div className="dateMade">
                    <p>
                        Date: {note.date}
                    </p>
                    <Link to={`/notes/${user.user_id}/${note.id}`}>Open note</Link>
                </div>

                </article>
            )}
        </section>
    );
}

export default AllNotes;