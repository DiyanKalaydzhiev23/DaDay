import { useState } from 'react';
import { useEffect } from 'react';
import { notesService } from '../../services/notesService';
import ReportChart from './ReportChart';

const MonthlyReport = () => {
    const user = localStorage.getItem('user') ? JSON.parse(localStorage.getItem('user')) : null;

    const [emotions, setEmotions] = useState([]);
    const [isLoading, setIsLoading] = useState(false);

    useEffect(() => {
        setIsLoading(true);

        notesService.getReport(user.user_id)
            .then(response => {
                console.log(response);
                setEmotions(response);
                setIsLoading(false);
            })
            .catch(err => {
                console.log(err);
            })
    }, [user.user_id]);

    return (
        <>  
            {isLoading && <p>Loading...</p>}
            {!isLoading && 
                <section className="flex flex-col items-center pb-10">
                    <h1 className="title mb-20">Monthly report</h1>

                    <ReportChart emotions={emotions}></ReportChart>
                </section>
            }   
        
        </>
    )

}

export default MonthlyReport;