<template>
  <b-card no-body>
    <b-card-header>
      <b-nav card-header tabs>
        <b-nav-item>
          <router-link active-class="active" to="/draw">
            Draw
          </router-link>
        </b-nav-item>
        <b-nav-item>
          <router-link active-class="active" to="/upload">
            Upload
          </router-link>
        </b-nav-item>
        <b-nav-item>
          <router-link active-class="active" to="/doc">
            API Documentation
          </router-link>
        </b-nav-item>
      </b-nav>
    </b-card-header>
    <b-card-body>
      <slot/>
    </b-card-body>
  </b-card>
</template>

<script setup lang='ts'>
import {
  BCard,
  BCardBody,
  BCardHeader,
  BNav,
  BNavItem
} from "bootstrap-vue-3";</script>

<style scoped>
.active {
  color: #6c757d;
}
</style>