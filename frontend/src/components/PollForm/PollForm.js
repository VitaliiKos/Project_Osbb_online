import React, {useEffect, useState} from 'react';
import {useForm} from "react-hook-form";

import {useDispatch, useSelector} from "react-redux";
import {pollActions} from "../../redux";
import css from './pollForm.module.css'

const PollForm = ({setStatusPoll}) => {
    const initialChoicesData = {
        question: 'Тема', description: 'Опис', choices: [{choice_text: 'Cтворіть варіант'}],
    };
    const {pollForUpdate} = useSelector(state => state.polls);
    const dispatch = useDispatch();
    const {register, handleSubmit, setValue, reset} = useForm();
    const [choicesData, setChoicesData] = useState(initialChoicesData);


    useEffect(() => {
        if (pollForUpdate) {
            setValue('question', choicesData.question);
            setValue('description', choicesData.description);
            choicesData.choices.forEach((choice, index) => {
                setValue(`choices[${index}].choice_text`, choice.choice_text);
            });

        }
    }, [setChoicesData, setValue, choicesData])


    const onSubmit = (poll) => {
        if (pollForUpdate) {
            const pollId = pollForUpdate.id
            dispatch(pollActions.updatePoll({pollId, poll}));
            dispatch(pollActions.setPollForUpdate(null))
        } else {
            dispatch(pollActions.createPoll(poll))

        }
        reset()
        resetChoicesData()
        setStatusPoll(false)
        dispatch(pollActions.getAll({'page': 1}))


        console.log(poll);
    };


    const addNewChoice = () => {
        const newChoice = {'choice_text': ''};
        setChoicesData(prevState => ({...prevState, choices: [...prevState.choices, newChoice]}));
        console.log(choicesData)
    }

    const removeChoice = (index) => {
        const newChoices = choicesData.choices;
        newChoices.splice(index, 1);
        console.log(index)
        console.log(newChoices)
        setChoicesData(prevState => ({...prevState, choices: newChoices}));
        console.log(choicesData)
    };
    const resetChoicesData = () => {
        setChoicesData(initialChoicesData);
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
                            {choicesData.choices.map((choice, index) => (<div key={index}>
                                <input type="text" {...register(`choices[${index}].choice_text`)}
                                       placeholder={'choice text'}/>
                            </div>))}
                        </div>

                    </div>
                    <button>{pollForUpdate ? 'Змінити' : 'Створити'}</button>
                </form>
            </div>

            <div className={css.addRemoveChoice}>
                {choicesData.choices.map((choice, index) => (<div key={index}>
                    <button onClick={() => removeChoice(index)}>-</button>
                </div>))}

                <button onClick={() => addNewChoice()}>Додати варіант</button>
            </div>
        </div>);
};
export {PollForm};