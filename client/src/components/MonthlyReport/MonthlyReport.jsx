import { useState } from 'react';
import { useEffect } from 'react';
import { notesService } from '../../services/notesService';

const MonthlyReport = () => {
    // const user = JSON.parse(localStorage.getItem('user'));
    // const userId = user.id;

    const [notes, setNotes] = useState([]);
    const [isLoading, setIsLoading] = useState(false);

    useEffect(() => {
        setIsLoading(true);

        notesService.getReport('4')
            .then(response => {
                console.log(response);
                setNotes(response);
                setIsLoading(false);
            })
            .catch(err => {
                console.log(err);
            })
            // [
            //     { id: 1, desc: 'I felt sad', emotion: 2, date: '2022-02-10' },
            //     { id: 2, desc: 'I felt happy', emotion: 5, date: '2022-01-23' }
            // ]

    }, []);

    return (
        <>  
            {isLoading && <p>Loading...</p>}
            {!isLoading && 
                <section>
                    <h1>Monthly report</h1>

                    <article>
                        {notes.map((note, i) => 
                            <section key={i}>
                                <p>{note.description}</p>    
                                <p>{note.emoji}</p>
                            </section>
                        )}
                    </article>
                </section>
            }   
        
        </>
    )

}

export default MonthlyReport;