import React, {useEffect} from 'react';
import {useForm} from "react-hook-form";

import {useDispatch, useSelector} from "react-redux";
import {pollActions} from "../../redux";
import css from './pollForm.module.css'

const PollForm = ({setStatusPoll}) => {
    const {pollForUpdate} = useSelector(state => state.polls);
    const dispatch = useDispatch();
    const {register, handleSubmit, setValue, reset} = useForm();


    useEffect(() => {
        if (pollForUpdate) {
            setValue('question', pollForUpdate.question);
            setValue('description', pollForUpdate.description);
            pollForUpdate.choices.forEach((choice, index) => {
                setValue(`choices[${index}].choice_text`, choice.choice_text);
            });

        }
    }, [setValue])


    const onSubmit = (poll) => {
        if (pollForUpdate) {
            const pollId = pollForUpdate.id
            dispatch(pollActions.updatePoll({pollId, poll}));
            dispatch(pollActions.setPollForUpdate(null))
        } else {
            console.log(poll)
            dispatch(pollActions.createPoll({poll}))

        }
        reset()
        setStatusPoll(false)
        dispatch(pollActions.getAll({'page': 1}))
        console.log(poll);
    };

    return (

        <div>
            <div className={css.formWrapper}>
                <form onSubmit={handleSubmit(onSubmit)}>
                    <div className={css.inputWrapper}>
                        <div>
                            <input type="text" {...register('question')} placeholder={'question'}/>
                        </div>

                        <div>
                            <input type="text" {...register('description')} placeholder={'description'}/>
                        </div>

                        <div>
                            <input type="text" {...register(`choices[${0}].choice_text`)} defaultValue={'За'}/>
                        </div>
                         <div>
                            <input type="text" {...register(`choices[${1}].choice_text`)} defaultValue={'Проти'}/>
                        </div>
                         <div>
                            <input type="text" {...register(`choices[${2}].choice_text`)} defaultValue={'Нейтрально'}/>
                        </div>

                    </div>
                    <button>{pollForUpdate ? 'Змінити' : 'Створити'}</button>
                </form>
            </div>

        </div>);
};
export {PollForm};