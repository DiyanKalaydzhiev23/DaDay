import { useState } from 'react';
import { useEffect } from 'react';
import { notesService } from '../../services/notesService';

const MonthlyReport = () => {
    const user = JSON.parse(localStorage.getItem('user'));
    const userId = user.id;

    const [notes, setNotes] = useState([]);
    const [isLoading, setIsLoading] = useState(false);

    useEffect(async () => {
        setIsLoading(true);

        try {
            const response = await notesService.getReport(userId);
            // [
            //     { id: 1, desc: 'I felt sad', emotion: 2, date: '2022-02-10' },
            //     { id: 2, desc: 'I felt happy', emotion: 5, date: '2022-01-23' }
            // ]
            console.log(response);
            setNotes(response);

            setIsLoading(false);
        } catch (err) {
            console.log(err);
        }
    }, [userId]);

    return (
        <>  
            {isLoading && <p>Loading...</p>}
            {!isLoading && 
                <section>
                    <h1>Monthly report</h1>

                    <article>
                        {notes.map(note => 
                            <p>{note.description}</p>    
                        )}
                    </article>
                </section>
            }   
        
        </>
    )

}