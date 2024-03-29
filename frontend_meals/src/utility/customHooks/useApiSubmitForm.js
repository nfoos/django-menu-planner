import { useState } from "react";
import { useStore } from "../formOnChangeReducer";
import { useAuthStore } from "../reducers/auth";
import { storage } from "../services/firebase/firebase.utility";
import Cookies from "js-cookie";
import axios from "../axios.orders";

const useSubmitForm = (props) => {
  const [state, dispatch] = useStore();
  const [authState, authDispatch] = useAuthStore();
  //const [progress, setProgress] = useState(0);
  const [error, setError] = useState("");

  const menu_id = authState.menu_id;

  const handleFormSubmit = async (e, data, currentMeals) => {
    let image = data?.img;

    e.preventDefault();
    const config = {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        "X-CSRFToken": Cookies.get("csrftoken"),
      },
    };

    try {
      if (image) {
        const uploadTask = storage.ref(`images/${image?.name}`).put(image);
        uploadTask.on(
          "state_changed",
          (snap) => {},
          (error) => {
            setError(error);
          },
          () => {
            storage
              .ref("images")
              .child(image.name)
              .getDownloadURL()
              .then(async (url) => {
                const testData = {
                  id: "",
                  date: data?.date,
                  type: data?.type.toLowerCase(),
                  menu: menu_id,
                  items: [
                    {
                      id: "",
                      name: data?.mealItem,
                      is_vegetarian: data?.is_vegetarian,
                      is_gluten_free: data?.is_gluten_free,
                      is_dairy_free: data?.is_dairy_free,
                      type: data?.mealType,
                      url: url,
                    },
                  ],
                };
                const body = JSON.stringify(testData);
                const res = await axios.post(
                  `menus/${menu_id}/meals/`,
                  body,
                  config
                );

                dispatch({
                  type: "RESPONSE_DATA",
                  payload: res?.data?.success,
                });
              });
          }
        );
      } else {
        const testData = {
          id: "",
          date: data?.date,
          type: data?.type.toLowerCase(),
          menu: menu_id,
          items: [
            {
              id: "",
              name: data?.mealItem,
              is_vegetarian: data?.is_vegetarian,
              is_gluten_free: data?.is_gluten_free,
              is_dairy_free: data?.is_dairy_free,
              type: data?.mealType,
              url: "",
            },
          ],
        };
        const body = JSON.stringify(testData);
        const res = await axios.post(`menus/${menu_id}/meals/`, body, config);
        dispatch({ type: "RESPONSE_DATA", payload: await res?.data?.success });
      }
    } catch (error) {
      console.log(error);
    }
  };

  const handleDelete = async (mealId, mealItemId) => {
    const data = { data: mealItemId };
    const body = JSON.stringify(data);

    const config = {
      method: "DELETE",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        "X-CSRFToken": Cookies.get("csrftoken"),
      },
      data: body,
    };
    const res = await axios
      .delete(`meal_items/${mealItemId}/`, config)
      .then((res) => {
        dispatch({ type: "RESPONSE_DATA", payload: res?.data?.success });
      });
  };

  const handleEdit = async (data) => {
    const image = data?.img;

    try {
      if (image) {
        const uploadTask = storage.ref(`images/${image?.name}`).put(image);
        uploadTask.on(
          "state_changed",
          (snap) => {},
          (error) => {
            setError(error);
          },
          () => {
            storage
              .ref("images")
              .child(image.name)
              .getDownloadURL()
              .then(async (url) => {
                const testData = {
                  id: data?.id,
                  name: data?.mealItem,
                  is_vegetarian: data?.is_vegetarian,
                  is_gluten_free: data?.is_gluten_free,
                  is_dairy_free: data?.is_dairy_free,
                  type: data?.mealType,
                  url: url,
                };

                const body = JSON.stringify(testData);
                const config = {
                  method: "PUT",
                  headers: {
                    Accept: "application/json",
                    "Content-Type": "application/json",
                    "X-CSRFToken": Cookies.get("csrftoken"),
                  },
                };
                const res = await axios
                  .put(`meal_items/${data?.id}/`, body, config)
                  .then((res) => {
                    dispatch({
                      type: "RESPONSE_DATA",
                      payload: res?.data?.success,
                    });
                  });
              });
          }
        );
      } else {
        const testData = {
          id: data?.id,
          name: data?.mealItem,
          is_vegetarian: data?.is_vegetarian,
          is_gluten_free: data?.is_gluten_free,
          is_dairy_free: data?.is_dairy_free,
          type: data?.mealType,
          url: "",
        };

        const body = JSON.stringify(testData);
        const config = {
          method: "PUT",
          headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
            "X-CSRFToken": Cookies.get("csrftoken"),
          },
        };
        const res = await axios
          .put(`meal_items/${data?.id}/`, body, config)
          .then((res) => {
            dispatch({ type: "RESPONSE_DATA", payload: res?.data?.success });
          });
      }
    } catch (error) {
      console.log(error);
    }
  };

  return [handleFormSubmit, handleDelete, handleEdit];
};

export default useSubmitForm;
