import pickle
import streamlit as st

# Load your pickled model
with open('pic.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

st.title("Welcome to the prediction of Compression Strength")

Material_Quantity = st.text_input("Material_Quantity")
Additive_Catalyst  = st.text_input("Additive_Catalyst")       
Ash_Component  = st.text_input("Ash_Component")          
Water_Mix  = st.text_input("Water_Mix")               
Plasticizer  = st.text_input("Plasticizer")          
Moderate_Aggregator  = st.text_input("Moderate_Aggregator")         
Refined_Aggregator  = st.text_input("Refined_Aggregator")          
Formulation_Duration  = st.text_input("Formulation_Duration")  


if st.button('Predict'):
    try:
        Material_Quantity = float(Material_Quantity)   
        Additive_Catalyst = float(Additive_Catalyst)          
        Ash_Component     = float(Ash_Component)          
        Water_Mix        = float(Water_Mix)            
        Plasticizer      = float(Plasticizer)            
        Moderate_Aggregator = float(Moderate_Aggregator)             
        Refined_Aggregator  = float(Refined_Aggregator)             
        Formulation_Duration   = float(Formulation_Duration)      
        
        IV = [[Material_Quantity,Additive_Catalyst,Ash_Component,Water_Mix,Plasticizer,Moderate_Aggregator,
               Refined_Aggregator,Formulation_Duration]]
        
        predict = model.predict(IV)

        st.write(f"The Compression Strength is => {predict}")
    except:
        st.write("Provide proper details")

